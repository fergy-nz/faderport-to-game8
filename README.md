# faderport-to-game8

Use your Presonus [FaderPort] as an 8 axis, 16 button game controller for
Windows. This application acts as a feeder to the fantastic [vJoy]
joystick emulation software.
For example you could map four of the axes to throttle controls and the
other four to propeller pitch in a multi-engine flight simulation.

The *Mix*, *Proj*, *Trns*, *Undo*, *Shift*, *Punch*, *User* and *Loop*
buttons are the *axes elect buttons*. The other 16 buttons act as standard
vJoy buttons.

Press the axes select button for the axis you want to control.
If you hold several down at once you can adjust multiple axes at the same
time. As you switch between axes the fader will jump to the remembered
position for each axis.

Use the fader or the Pan knob to adjust the selected axes.

NOTE! Due to a quirk in the FaderPort's implementation, if you hold the
'Off' button down the fader won't report any movement.

# Requirements
* A Presonus [FaderPort] connected to your Windows computer.
* [vJoy] installed with the first [vJoy] device configured as an 8 axes,
  16 button device.
* An installed [Python 3.6] interpreter.
* My [faderport-1.0.1] python module installed. Use:
  ```sh
  pip install faderport
  ```
  (This should also install the required [mido] and [python-rtmidi] modules.)
* This *faderport-to-game8* repo.

# Installation
There's a [video](https://youtu.be/0sSXrUWEO40) showing a full installation
and configuration, but essentially you just:
1. Download and Install the [FaderPort] drivers (if you haven't already)
2. Download and Install [vJoy]
3. Download and Install Python 3.6 (or later). Adding it to your path will
   make it easier to run the faderport-to-game8 script later.

4. Install the following python module: [faderport-1.0.1]
   This can be done at a command prompt, using:
   ```sh
   pip install faderport
   ```
   This should also install the required [mido] and [python-rtmidi] modules.
5. Download or clone the contents of this repo.

# Configuration
[vJoy] must be configured with device #1 set for 8 axes, 16 buttons and
0 POVs. On my machine it looks like this:

![Sample vJoy Configuration Image][vJoyConfSampleImg]

# Running
Run the script with:
```sh
python faderport-to-game8.py
```
Enjoy !!!

# Disclaimer
You use this entirely at your own risk.
I run it on my Windows 10 Home PC and haven't had any problems
but that doesn't mean that you won't.
Use your own judgement, the source code is right there for you to examine.

[FaderPort]: https://www.presonus.com/products/faderport
[vJoy]: http://vjoystick.sourceforge.net/site/
[Python 3.6]: https://www.python.org/
[faderport-1.0.1]: https://pypi.org/project/faderport/
[mido]: https://pypi.org/project/mido/
[python-rtmidi]: https://pypi.org/project/python-rtmidi/
[vJoyConfSampleImg]: vJoy-Configuration.png