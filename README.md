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
then map to whatever you like in your game/simulation of choice.

The Pan knob is configured to act as a fine tuner for the active axis.

# Requirements
* A Presonus [FaderPort] connected to your Windows computer.
* An installed [Python 3.6] interpreter.
* [vJoy] installed with the first [vJoy] device configured as an 8 axes,
  16 button device.
* My [faderport-1.0.1] python module installed. Use: `pip install faderport`

  (This should also install the required [mido] and [python-rtmidi] modules.)
* This faderport-to-game8 repo.

# Installation
There are two options...
### Option A - Easy - 64 Bit Windows 10 Only
If you're running 64 bit Windows 10 you can:
1. Download and install [vJoy]
2. Download and unzip this self-contained executable file.

The executable was built with PyInstaller using the following command line:

```sh
pyinstaller --onefile --hidden-import mido.backends.rtmidi --add-binary vJoyInterface.dll;. faderport-to-game8.py
```

### Option B - One bit at a time - Windows 7, 8 or 10
1. Install [vJoy]
2. Install [Python 3.6] - Just run the installer. I think there's an option
   to add it to your PATH, you should do that.
3. Install the following python modules: [faderport-1.0.1]
   This can be done at a command prompt, using:
   '''sh
   pip install faderport mido python-rtmidi
   '''
   This should also install the required [mid] and [python-rtmidi] modules.
4. Download or clone the contents of this repo.

# Configuration
[vJoy] must be configured with device #1 set for 8 axes, 16 buttons and
0 POVs. On my machine it looks like this:

![Sample vJoy Configuration Image][vJoyConfSampleImg]


[FaderPort]: https://www.presonus.com/products/faderport
[vJoy]: http://vjoystick.sourceforge.net/site/
[Python 3.6]: https://www.python.org/
[faderport-1.0.1]: https://pypi.org/project/faderport/
[mido]: https://pypi.org/project/mido/
[python-rtmidi]: https://pypi.org/project/python-rtmidi/
[vJoyConfSampleImg]: vJoy-Configuration.png