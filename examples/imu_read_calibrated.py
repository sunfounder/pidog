#!/usr/bin/env python3
''' PiDog IMU (SH3001) - read the calibrated values

    Companion to examples/imu_calibration.py.

    This script prints the IMU readings in physical units, using the
    calibration stored in the pidog config file:

        acc  -> [x, y, z] in g
        gyro -> [x, y, z] in deg/s

    The library call behind it is:

        acc, gyro = my_dog.imu.get_calibrated_data()

    which corrects every axis with:   value = (raw - bias) / scale
    ('scale' being the real sensitivity of that axis, in LSB per g for the
    accelerometer and LSB per deg/s for the gyroscope).  Without a stored
    calibration the datasheet nominal values are used
    (16384 LSB/g at +-2g, 16.4 LSB/deg/s at +-2000 dps).

    What to expect:

      * resting on a level surface, the printed acceleration vector
        magnitude should be 1.000 g and the gyro readings close to
        0 deg/s;
      * the 'gain ratio' printed below compares the stored sensitivity with
        the datasheet nominal.  A value far from 1.000 means the module has
        a gain error.  A gain error does not affect the attitude angles
        (they are ratios) but it does corrupt the absolute g values, and an
        offset-only calibration can never correct it -- run
        examples/imu_calibration.py to measure and store the real
        sensitivity.

    Run:
        sudo python3 examples/imu_read_calibrated.py
'''

from pidog import Pidog
from time import sleep

SAMPLE_COUNT = 100          # samples used for the summary
SAMPLE_INTERVAL = 0.02      # seconds between samples

NOMINAL_ACC_SCALE = 16384.0  # datasheet sensitivity, +-2g range


def have_imu(my_dog):
    '''Pidog only sets self.imu when the SH3001 init succeeds.'''
    return hasattr(my_dog, 'imu')


def print_calibration(imu):
    '''Print the calibration that is currently in use.'''
    nominal = [abs(s - NOMINAL_ACC_SCALE) < 1e-6 for s in imu.acc_scale]
    print('--- calibration in use ---')
    print('acc_bias  (LSB)   : %s' % imu.acc_bias)
    print('acc_scale (LSB/g) : %s' % imu.acc_scale)
    print('gyro_bias (LSB)   : %s' % imu.gyro_bias)
    print('gyro_scale        : %s' % imu.gyro_scale)
    print('gain ratio        : %s' %
          [round(s / NOMINAL_ACC_SCALE, 4) for s in imu.acc_scale])
    if all(nominal):
        print('=> no accelerometer calibration stored, using the datasheet'
              ' nominal sensitivity')
    else:
        print('=> stored calibration is being applied')
    print('')


def read_summary(my_dog):
    '''Average the calibrated readings over a short window and print a
    summary plus a verdict.'''
    acc_sum = [0.0, 0.0, 0.0]
    gyro_sum = [0.0, 0.0, 0.0]
    count = 0
    print('Sampling %d calibrated readings, keep the dog still ...' %
          SAMPLE_COUNT)
    for _ in range(SAMPLE_COUNT):
        data = my_dog.imu.get_calibrated_data()
        if data is False:
            continue
        acc, gyro = data
        for axis in range(3):
            acc_sum[axis] += acc[axis]
            gyro_sum[axis] += gyro[axis]
        count += 1
        sleep(SAMPLE_INTERVAL)
    if count == 0:
        print('ERROR: no IMU data could be read')
        return
    acc = [acc_sum[axis] / count for axis in range(3)]
    gyro = [gyro_sum[axis] / count for axis in range(3)]
    mag = (acc[0] ** 2 + acc[1] ** 2 + acc[2] ** 2) ** 0.5
    print('')
    print('--- calibrated result (mean of %d samples) ---' % count)
    print('acc  (g)     : %8.4f %8.4f %8.4f' % (acc[0], acc[1], acc[2]))
    print('|a|  (g)     : %8.4f' % mag)
    print('gyro (deg/s) : %8.4f %8.4f %8.4f' % (gyro[0], gyro[1], gyro[2]))
    print('')
    error = abs(mag - 1.0)
    if error <= 0.02:
        print('=> OK: resting magnitude is 1.000 g (within 2%%),'
              ' the accelerometer scale is good.')
    elif error <= 0.10:
        print('=> MARGINAL: resting magnitude is %.3f g, %.1f%% away from' %
              (mag, error * 100.0))
        print('   1.000 g. Consider running examples/imu_calibration.py.')
    else:
        print('=> NOT CALIBRATED: resting magnitude is %.3f g (expected' % mag)
        print('   1.000 g, %.1f%% off).  The absolute g values cannot be' %
              (error * 100.0))
        print('   trusted until examples/imu_calibration.py has been run on'
              ' this unit.')
    print('')


def show_live(my_dog):
    '''Continuously print the calibrated readings until Ctrl+C.'''
    print('--- live calibrated readings (Ctrl+C to quit) ---')
    while True:
        data = my_dog.imu.get_calibrated_data()
        if data is False:
            continue
        acc, gyro = data
        mag = (acc[0] ** 2 + acc[1] ** 2 + acc[2] ** 2) ** 0.5
        print('acc: %7.3f %7.3f %7.3f g (|a| = %5.3f g)  '
              'gyro: %8.2f %8.2f %8.2f deg/s' %
              (acc[0], acc[1], acc[2], mag, gyro[0], gyro[1], gyro[2]),
              end='\r')
        sleep(SAMPLE_INTERVAL)


def main():
    my_dog = Pidog()
    sleep(2)

    try:
        if not have_imu(my_dog):
            print('ERROR: SH3001 IMU is not available (init failed).')
            print('       Check the IMU connection, and run this script with')
            print('       sudo so that i2cdetect is found in PATH.')
            return

        print_calibration(my_dog.imu)
        read_summary(my_dog)
        show_live(my_dog)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print('\033[31mERROR: %s\033[m' % e)
    finally:
        my_dog.close()


if __name__ == '__main__':
    main()
