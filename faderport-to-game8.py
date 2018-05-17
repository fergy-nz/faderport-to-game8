import time

from faderport import FaderPort, button_from_name
from vjoy import vjoy, HIDUsage

PAN_SCALE = 128

# This is the list of buttons that we map to vJoy buttons
gameButtons = [
    button_from_name("Mute"),
    button_from_name("Solo"),
    button_from_name("Rec Arm"),
    button_from_name("Chan Down"),
    button_from_name("Bank"),
    button_from_name("Chan Up"),
    button_from_name("Output"),
    button_from_name("Read"),
    button_from_name("Write"),
    button_from_name("Touch"),
    button_from_name("Off"),
    button_from_name("Rewind"),
    button_from_name("Fast Fwd"),
    button_from_name("Stop"),
    button_from_name("Play"),
    button_from_name("Record")
]

# This is the list of buttons we map to fader axis selection
faderButtons = [
    button_from_name("Mix"),
    button_from_name("Proj"),
    button_from_name("Trns"),
    button_from_name("Undo"),
    button_from_name("Shift"),
    button_from_name("Punch"),
    button_from_name("User"),
    button_from_name("Loop"),
]


class GameFaderPort8(FaderPort):
    def __init__(self):
        super().__init__()
        self.acquired = False
        self.active = 0
        self.pressed = []
        self.axes = [
            [HIDUsage.X.value, 16384],
            [HIDUsage.Y.value, 16384],
            [HIDUsage.Z.value, 16384],
            [HIDUsage.RX.value, 16384],
            [HIDUsage.RY.value, 16384],
            [HIDUsage.RZ.value, 16384],
            [HIDUsage.SL0.value, 16384],
            [HIDUsage.SL1.value, 16384],
        ]

    def on_open(self):
        # Try to acquire the vJoy
        if vjoy.vJoyEnabled() and vjoy.AcquireVJD(1):
            self.acquired = True

            # Set all buttons off
            for b in range(16):
                vjoy.SetBtn(False, 1, b + 1)

            # Set axes
            # for a in range(8):
            #     vjoy.SetAxis(self.axes[a][1], 1, self.axes[a][0])
            self.reset_vjoy_axes()

            self.x = 16384

            self.countdown(.5)
            self.light_on(faderButtons[self.active])
        else:
            print('Could not acquire the vJoy device.\n'
                  'Is vJoy installed and configured?\n'
                  'Is vJoy device #1 configured for 8 axes, 16 buttons and no POVs?')

    def on_rotary(self, direction):
        """Rotary changes will fine tune the fader position."""
        if direction > 0:  # Clockwise
            if self.axes[self.active][1] < 32768 - PAN_SCALE:
                value = self.axes[self.active][1] + PAN_SCALE
            else:
                value = 32768
        else:  # Counter-clockwise
            if self.axes[self.active][1] >= PAN_SCALE:
                value = self.axes[self.active][1] - PAN_SCALE
            else:
                value = 0

        if self.pressed:
            for i in self.pressed:
                self.axes[i][1] = value
                vjoy.SetAxis(value, 1, self.axes[i][0])
        else:
            self.axes[self.active][1] = value
            vjoy.SetAxis(value, 1, self.axes[self.active][0])

        self.x = value

    def on_fader(self, value):
        if self.pressed:
            for i in self.pressed:
                self.axes[i][1] = self.x
                vjoy.SetAxis(self.x, 1, self.axes[i][0])
        else:
            self.axes[self.active][1] = self.x
            vjoy.SetAxis(self.x, 1, self.axes[self.active][0])

    def reset_vjoy_axes(self):
        for ax in self.axes:
            vjoy.SetAxis(16384, 1, ax[0])

    def on_fader_touch(self, state):
        if self.pressed and state:
            for i in self.pressed:
                if i != self.active:
                    self.axes[i][1] = self.axes[self.active][1]
                    vjoy.SetAxis(self.axes[self.active][1], 1, self.axes[self.active][0])

    def on_button(self, button, state):
        if button in gameButtons:
            btn = 1 + gameButtons.index(button)
            vjoy.SetBtn(state, 1, btn)
        elif button in faderButtons:
            sel = faderButtons.index(button)
            if state:
                self.light_on(faderButtons[sel])
                self.pressed.append(sel)
                if self.active not in self.pressed:
                    self.light_off(faderButtons[self.active])
                    self.active = sel
                    self.x = self.axes[sel][1]
            else:
                self.pressed.remove(sel)
                self.active = self.pressed[0] if self.pressed else sel
                if self.active != sel:
                    self.light_off(faderButtons[sel])

    @property
    def x(self):
        """Convert FaderPort units to vJoy units"""
        return (1 + self.fader) * 32

    @x.setter
    def x(self, value):
        """Convert vJoy units to FaderPort units and adjust fader position."""
        self.fader = (value >> 5) - 1

    def on_close(self):
        self.reset_vjoy_axes()
        # Release the vJoy
        if self.acquired:
            vjoy.RelinquishVJD(1)
        print('Shutting down faderport-to-game8.')


if __name__ == '__main__':
    doc = """\
FaderPort to Game8 — An 8 Axis, 16 button vJoy Feeder Application
Copyright © jayferg 2018

The 'Mix', 'Proj', 'Trns', 'Undo', 'Shift', 'Punch', 'User' and 'Loop' buttons
are the 'Axes Select Buttons'. The other 16 buttons act as standard vJoy buttons.

Press the axes select button for the axis you want to control.
If you hold several down at once you can adjust multiple axes at the same time.

Use the fader or the Pan knob to adjust the selected axes.

NOTE! Due to a quirk in the FaderPort's implementation, if you hold the
'Off' button down the fader won't report any movement.

Have fun and hit Ctrl-C to exit...     
"""
    print(doc)
    with GameFaderPort8() as fp:
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            pass
