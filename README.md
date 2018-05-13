# faderport-to-game8
Use your Presonus [FaderPort] as an 8 axis, 16 button game controller for
Windows. This application acts as a feeder to the fantastic [vJoy]
joystick emulation software.
For example you could map four of the axes to throttle controls and the
other four to propeller pitch in a multi-engine flight simulation.

Obviously the [FaderPort] only has a single fader so you can only adjust
a single axis at a time. The app remembers the current position setting
for each of the 8 axes. You use the *Mix*, *Proj*, *Trns*, *Undo*, *Shift*,
*Punch*, *User* and *Loop* buttons to select the active axis. The button
corresponding to the active axis will be lit. As you switch between axes
the fader will jump to the remembered position for each axis.

The remaining 16 buttons are mapped as joystick buttons which you can
then map to whatever you like.

The Pan knob is configured to act as a fine tune for the active axis.

# Requirements
* A Presonus [FaderPort], connected to your Windows computer.
* An installed [Python 3.6] interpreter.
* [vJoy] installed with the first [vJoy] device configured as an 8 axes,
  16 button device.
* My [faderport-1.0.0] python module installed (`pip install faderport`)
* This faderport-to-game8 application.

# Installation
TODO

[FaderPort]: https://www.presonus.com/products/faderport
[vJoy]: http://vjoystick.sourceforge.net/site/
[Python 3.6]: https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe
[faderport-1.0.0]: https://pypi.org/project/faderport/