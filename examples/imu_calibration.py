#!/usr/bin/env python3
''' PiDog IMU (SH3001) calibration example

    Calibrates the SH3001 6-axis IMU with the standard two-step procedure and
    saves the result into the pidog config file, so the calibrated values can
    be read back later through the IMU library:

        acc, gyro = my_dog.imu.get_calibrated_data()
            acc  -> [x, y, z] in g
            gyro -> [x, y, z] in deg/s

    Procedure:

      1. Gyroscope (static): keep the dog completely still and average the
         gyro readings to obtain the zero-rate bias.

      2. Accelerometer (rotation): rotate the dog so that every axis sees
         both +1g and -1g.  Two ways work:

             - a figure-8 (8-shape), or
             - two full turns around each of the X, Y and Z axes.

         The live min/max of every axis is displayed while you rotate; press
         Enter when all three axes show [ok].  There is no time limit.
         For each axis:

             bias  = (max + min) / 2      zero-g offset
             scale = (max - min) / 2      real sensitivity, in LSB per g

         The scale is the part an offset-only calibration can never obtain:
         the datasheet nominal is 16384 LSB/g at +-2g, but an individual
         module may have a gain error.  A gain error does not affect the
         attitude angles (they are ratios), but it does corrupt the absolute
         g values, so it must be measured with the rotation.
         After the calibration, an accelerometer at rest should read a
         vector magnitude of 1.000 g.

    NOTE: this calibration is for reading physical values from the raw
    sensor.  The Pidog program itself uses its own still-and-level
    auto-calibration at startup (Pidog.imu_acc_offset), which this example
    does not change.

    Re-running the calibration always starts from scratch and overwrites the
    stored values (it never accumulates).  To clear the calibration and go
    back to the datasheet nominal values:

        sudo python3 examples/imu_calibration.py --reset

    Run:
        sudo python3 examples/imu_calibration.py
'''

import select
import sys
import textwrap
from time import sleep, time

from pidog import Pidog

GYRO_SAMPLES = 200          # static gyro samples
GYRO_INTERVAL = 0.02        # seconds between gyro samples

ACC_INTERVAL = 0.02         # seconds between acc samples
ACC_MAX_SECONDS = 120       # safety stop if Enter is never pressed
ACC_FALLBACK_SECONDS = 15   # used when stdin is not a terminal (no Enter)

NOMINAL_ACC_SCALE = 16384.0  # datasheet sensitivity, +-2g range
COVERAGE_MIN_LSB = 0.8 * NOMINAL_ACC_SCALE  # axis counts as covered at +-0.8g

AXIS_NAME = ('X', 'Y', 'Z')
BOX_WIDTH = 66              # inner width of the instruction boxes


def have_imu(my_dog):
    '''Pidog only sets self.imu when the SH3001 init succeeds.'''
    return hasattr(my_dog, 'imu')


def clear_live_line():
    '''Erase the live status line so normal output stays clean.'''
    print('\r\033[K', end='', flush=True)


def print_box(title, lines=(), width=BOX_WIDTH):
    '''Print a boxed block of text, to keep the instructions clearly apart
    from the Pidog startup log.'''
    inner = width - 2
    rule = '+' + '-' * inner + '+'
    out = ['', rule]
    out.append('|' + (' ' + title).ljust(inner) + '|')
    out.append(rule)
    for line in lines:
        if not line:
            out.append('|' + ' ' * inner + '|')
            continue
        indent = len(line) - len(line.lstrip(' '))
        for part in textwrap.wrap(line.strip(), inner - 3 - indent) or ['']:
            out.append('|' + (' ' * (1 + indent) + part).ljust(inner) + '|')
    out.append(rule)
    out.append('')
    print('\n'.join(out))


def wait_for_key(prompt):
    '''Wait for the user to press Enter. In non-interactive sessions (EOF) it
    simply returns so the calibration can still proceed.'''
    try:
        input(prompt)
    except EOFError:
        pass


def enter_pressed():
    '''True when a line is already available on stdin (Enter was pressed).'''
    if not sys.stdin.isatty():
        return False
    try:
        return bool(select.select([sys.stdin], [], [], 0)[0])
    except (OSError, ValueError):
        return False


def acc_covered(acc_min, acc_max):
    '''Per axis: True when both +1g and -1g have been seen.'''
    return [
        acc_max[a] >= COVERAGE_MIN_LSB and acc_min[a] <= -COVERAGE_MIN_LSB
        for a in range(3)
    ]


def format_live(acc_min, acc_max, elapsed):
    '''One line showing the live min/max and coverage of every axis.'''
    covered = acc_covered(acc_min, acc_max)
    parts = []
    for a in range(3):
        lo = '    --' if acc_min[a] == float('inf') else '%6d' % acc_min[a]
        hi = '    --' if acc_max[a] == float('-inf') else '%6d' % acc_max[a]
        parts.append('%s: %s %s %s' %
                     (AXIS_NAME[a], lo, hi, '[ok]' if covered[a] else '[  ]'))
    return '  '.join(parts) + '   %5.1fs' % elapsed


def calibrate_gyro(my_dog):
    '''Static gyroscope calibration.

    Keep the dog completely still and average the raw gyro readings; the mean
    is the zero-rate bias.  Returns [x, y, z] in LSB.
    '''
    gyro_sum = [0.0, 0.0, 0.0]
    gyro_min = [float('inf')] * 3
    gyro_max = [float('-inf')] * 3
    print('  measuring, keep still ...')
    for _ in range(GYRO_SAMPLES):
        data = my_dog.imu._sh3001_getimudata()
        if data is False:
            print('  ERROR: IMU data read failed')
            return None
        _, gyro = data
        for axis in range(3):
            gyro_sum[axis] += gyro[axis]
            gyro_min[axis] = min(gyro_min[axis], gyro[axis])
            gyro_max[axis] = max(gyro_max[axis], gyro[axis])
        sleep(GYRO_INTERVAL)
    gyro_bias = [round(gyro_sum[axis] / GYRO_SAMPLES, 1) for axis in range(3)]
    print('  gyro noise (max-min): %s' %
          [gyro_max[axis] - gyro_min[axis] for axis in range(3)])
    return gyro_bias


def calibrate_acc(my_dog):
    '''Rotation accelerometer calibration.

    Rotate the dog until every axis has seen both +1g and -1g (a figure-8, or
    two full turns around each axis), watching the live min/max, then press
    Enter.  Returns (bias, scale): bias in LSB, scale in LSB per g.
    '''
    acc_min = [float('inf')] * 3
    acc_max = [float('-inf')] * 3

    tty = sys.stdin.isatty()
    limit = ACC_MAX_SECONDS if tty else ACC_FALLBACK_SECONDS
    if not tty:
        print('  (stdin is not a terminal, rotating for %ss)' % limit)

    print('')
    print('  live per-axis extremes (raw LSB), [ok] = saw +1g and -1g:')
    print('')

    start = time()
    last_draw = -1.0
    while True:
        data = my_dog.imu._sh3001_getimudata()
        if data is not False:
            acc, _ = data
            for axis in range(3):
                acc_min[axis] = min(acc_min[axis], acc[axis])
                acc_max[axis] = max(acc_max[axis], acc[axis])
        elapsed = time() - start
        if elapsed - last_draw >= 0.2:
            last_draw = elapsed
            print('\r  %s\033[K' % format_live(acc_min, acc_max, elapsed),
                  end='', flush=True)
        if elapsed > limit:
            print('')
            if tty:
                print('  WARNING: stopped after %ss (Enter was not pressed),' % limit)
                print('           using what was collected.')
            break
        if tty and enter_pressed():
            sys.stdin.readline()
            print('')
            break
        sleep(ACC_INTERVAL)

    if any(v == float('inf') for v in acc_min):
        print('  ERROR: no accelerometer samples collected')
        return None, None

    covered = acc_covered(acc_min, acc_max)
    if not all(covered):
        missing = [AXIS_NAME[a] for a in range(3) if not covered[a]]
        print('  WARNING: axis %s never reached both +1g and -1g, the scale' %
              ' '.join(missing))
        print('           for those axes may be inaccurate; consider running')
        print('           the calibration again.')
    acc_bias = [round((acc_max[a] + acc_min[a]) / 2.0, 1) for a in range(3)]
    acc_scale = [round((acc_max[a] - acc_min[a]) / 2.0, 1) for a in range(3)]
    return acc_bias, acc_scale


def show_live(my_dog):
    '''Print the calibrated live readings (acc in g, gyro in deg/s).'''
    print('')
    print('  live calibrated readings, Ctrl+C to quit:')
    print('')
    while True:
        data = my_dog.imu.get_calibrated_data()
        if data is False:
            continue
        acc, gyro = data
        mag = (acc[0] ** 2 + acc[1] ** 2 + acc[2] ** 2) ** 0.5
        print('\r  acc: %7.3f %7.3f %7.3f g  (|a| = %5.3f g)   '
              'gyro: %8.2f %8.2f %8.2f deg/s\033[K' %
              (acc[0], acc[1], acc[2], mag, gyro[0], gyro[1], gyro[2]),
              end='', flush=True)
        sleep(ACC_INTERVAL)


def clear_calibration(my_dog):
    '''Clear both calibrations: the sensor bias/scale measured by this script,
    and the Pidog still-and-level offsets.'''
    my_dog.imu.reset_calibration()
    my_dog.reset_imu_offsets()
    print_box('CALIBRATION CLEARED', [
        'acc_scale back to the datasheet nominal: %s' % my_dog.imu.acc_scale,
        'acc_bias  cleared: %s' % my_dog.imu.acc_bias,
        'gyro_scale back to nominal: %s' % my_dog.imu.gyro_scale,
        'gyro_bias cleared: %s' % my_dog.imu.gyro_bias,
        '',
        'get_calibrated_data() now uses the datasheet nominal sensitivity.',
        'The Pidog program will auto-calibrate its own still-and-level',
        'offsets at the next start-up.'])


def main():
    my_dog = Pidog()
    sleep(1)

    try:
        if not have_imu(my_dog):
            print('ERROR: SH3001 IMU is not available (init failed).')
            print('       Check the IMU connection, and run this script with')
            print('       sudo so that i2cdetect is found in PATH.')
            return

        imu = my_dog.imu

        # ---- optional: clear an existing calibration and exit ----
        if '--reset' in sys.argv[1:] or '-r' in sys.argv[1:]:
            clear_calibration(my_dog)
            return

        # ---- step 1: gyroscope (static) ----
        print_box('STEP 1/2   GYROSCOPE CALIBRATION  (static)',
                  ['Place the dog on a flat surface and keep it completely',
                   'still.  The zero-rate bias is measured from the still',
                   'readings (~4 seconds).'])
        wait_for_key('  >> press Enter to start: ')
        gyro_bias = calibrate_gyro(my_dog)
        if gyro_bias is None:
            return
        imu.set_gyro_calibration(bias=gyro_bias)

        # ---- step 2: accelerometer (rotation) ----
        print_box('STEP 2/2   ACCELEROMETER CALIBRATION  (rotation)',
                  ['Pick the dog up and rotate it so that every axis sees',
                   'both +1g and -1g.  Two ways work:',
                   '  - a figure-8 (8-shape), or',
                   '  - two full turns around each of the X, Y, Z axes.',
                   '',
                   'The live min/max of each axis is shown below.',
                   'Press Enter when all three axes show [ok].',
                   'There is no time limit - take as long as you need.'])
        wait_for_key('  >> press Enter to start: ')
        acc_bias, acc_scale = calibrate_acc(my_dog)
        if acc_bias is None:
            return
        imu.set_acc_calibration(bias=acc_bias, scale=acc_scale)

        print_box('CALIBRATION SAVED',
                  ['acc_bias  (LSB)   : %s' % acc_bias,
                   'acc_scale (LSB/g) : %s' % acc_scale,
                   'gyro_bias (LSB)   : %s' % gyro_bias,
                   'gain ratio        : %s' %
                   [round(s / NOMINAL_ACC_SCALE, 4) for s in acc_scale],
                   '',
                   'At rest on a level surface |a| should now read 1.000 g.',
                   'Read the calibrated values any time with:',
                   '    acc, gyro = my_dog.imu.get_calibrated_data()',
                   'Clear it again with:',
                   '    sudo python3 examples/imu_calibration.py --reset'])

        show_live(my_dog)
    except KeyboardInterrupt:
        clear_live_line()
        pass
    except Exception as e:
        clear_live_line()
        print('\033[31mERROR: %s\033[m' % e)
    finally:
        my_dog.close()


if __name__ == '__main__':
    main()
