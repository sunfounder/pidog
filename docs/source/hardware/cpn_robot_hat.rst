Robot HAT
-----------------------------


Robot HAT is a multifunctional expansion board that allows Raspberry Pi to be quickly turned into a robot. 
An MCU is on board to extend the PWM output and ADC input for the Raspberry Pi, 
as well as a motor driver chip, I2S audio module and mono speaker. 
As well as the GPIOs that lead out of the Raspberry Pi itself.

It also comes with a Speaker, 
which can be used to play background music, sound effects and implement TTS functions to make your project more interesting.

Accepts 7-12V PH2.0 5pin power input with 2 battery indicators, 1 charge indicator and 1 power indicator. 
The board also has a user available LED and a button for you to quickly test some effects.


.. image:: img/O1902V40RobotHAT.png

**Left/Right Motor Port**
    * 2-channel XH2.54 motor ports.
    * The left port is connected to GPIO 4 and the right port is connected to GPIO 5.

**I2C Pin/Port**
    * I2C pins from Raspberry Pi.

**SPI Pin**
    * SPI pins from Raspberry Pi.

**UART Pin**
    * UART pins from Raspberry Pi.

**PWM Pin**
    * 12-channel PWM pins, P0-P12.

**ADC Pin**
    * 4-channel ADC pins, A0-A3.

**Digital Pin**
    * 4-channel digital pins, D0-D3.

**Type-C USB Port**
    * Energize this port to activate the battery.
    * Used to charge the battery.

**Battery Indicator**
    * Two LEDs light up when the voltage is higher than 7.8V.
    * One LED lights up in the 6.7V to 7.8V range. 
    * Below 6.7V, both LEDs turn off.

**Power Indicator**
    * If Robot HAT is working, it lights up.

**Chip Work Indicator**
    * If Robot HAT chip is working, it lights up.

**Charge Indicator**
    * On when charging the battery.
    * Off when the battery is fully charged.

**User LED**
    * Set by your program. (Outputting 1 turns the LED on; Outputting 0 turns it off.)

**RST Button**
    * Short pressing RST Button causes program resetting.
    * Long press RST Button till the LED lights up then release, and you will disconnect the Bluetooth.

**USR Button**
    * The functions of USR Button can be set by your programming. (Pressing down leads to a input “0”; releasing produces a input “1”. ) 

**Power Switch**
    * Turn on/off the power of the robot HAT.
    * When you connect power to the power port, the Raspberry Pi will boot up. However, you will need to switch the power switch to ON to enable Robot HAT.

**Power Port**
    * 7-12V PH2.0 5pin power input.
    * Powering the Raspberry Pi and Robot HAT at the same time.