# Python wrapper on vJoy library
from _ctypes import byref
from ctypes import cdll, c_bool, c_short, c_char_p, c_wchar_p, c_int, c_long, c_uint, c_ubyte
from enum import Enum

import time

class HIDUsage(Enum):
    X = 0x30
    Y = 0x31
    Z = 0x32
    RX = 0x33
    RY = 0x34
    RZ = 0x35
    SL0 = 0x36
    SL1 = 0x37
    WHL = 0x38
    POV = 0x39

class VjdStat(Enum):
    VJD_STAT_OWN = 0  # The  vJoy Device is owned by this application.
    VJD_STAT_FREE = 1  # The  vJoy Device is NOT owned by any application (including this one).
    VJD_STAT_BUSY = 2  # The  vJoy Device is owned by another application. It cannot be acquired by this application.
    VJD_STAT_MISS = 3  # The  vJoy Device is missing. It either does not exist or the driver is down.
    VJD_STAT_UNKN = 4  # Unknown

class VJoy(object):
    def __init__(self):
        self._vjoy = cdll.LoadLibrary('vjoyinterface')

        # VJOYINTERFACE_API BOOL	__cdecl vJoyEnabled(void);
        self.vJoyEnabled = self._vjoy.vJoyEnabled
        self.vJoyEnabled.argtypes = None
        self.vJoyEnabled.restype = c_bool

        # VJOYINTERFACE_API SHORT __cdecl GetvJoyVersion(void);
        self.GetvJoyVersion = self._vjoy.GetvJoyVersion
        self.GetvJoyVersion.argtypes = None
        self.GetvJoyVersion.restype = c_short

        # VJOYINTERFACE_API PVOID	__cdecl	GetvJoyProductString(void);
        self.GetvJoyProductString = self._vjoy.GetvJoyProductString
        self.GetvJoyProductString.argtypes = None
        self.GetvJoyProductString.restype = c_wchar_p

        # VJOYINTERFACE_API PVOID	__cdecl	GetvJoyManufacturerString(void);
        self.GetvJoyManufacturerString = self._vjoy.GetvJoyManufacturerString
        self.GetvJoyManufacturerString.argtypes = None
        self.GetvJoyManufacturerString.restype = c_wchar_p

        # VJOYINTERFACE_API PVOID	__cdecl	GetvJoySerialNumberString(void);
        self.GetvJoySerialNumberString = self._vjoy.GetvJoySerialNumberString
        self.GetvJoySerialNumberString.argtypes = None
        self.GetvJoySerialNumberString.restype = c_wchar_p

        # VJOYINTERFACE_API VOID	__cdecl	RegisterRemovalCB(RemovalCB cb, PVOID data);

        # VJOYINTERFACE_API BOOL		__cdecl	AcquireVJD(UINT rID); # Acquire the specified vJoy Device.
        self.AcquireVJD = self._vjoy.AcquireVJD
        self.AcquireVJD.argtypes = [c_int, ]
        self.AcquireVJD.restype = c_bool

        # VJOYINTERFACE_API VOID		__cdecl	RelinquishVJD(UINT rID); # Relinquish the specified vJoy Device.
        self.RelinquishVJD = self._vjoy.RelinquishVJD
        self.RelinquishVJD.argtypes = [c_int, ]
        self.RelinquishVJD.restype = c_bool

        # VJOYINTERFACE_API BOOL __cdecl SetAxis(LONG Value, UINT rID, UINT Axis);		// Write Value to a given axis defined in the specified VDJ
        self.SetAxis = self._vjoy.SetAxis
        self.SetAxis.argtypes = [c_long, c_uint, c_uint]
        self.SetAxis.restype = c_bool

        # VJOYINTERFACE_API BOOL __cdecl SetBtn(BOOL Value, UINT rID, UCHAR nBtn);		// Write Value to a given button defined in the specified VDJ
        self.SetBtn = self._vjoy.SetBtn
        self.SetBtn.argtypes = [ c_bool, c_uint, c_ubyte]
        self.SetBtn.restype = c_bool

        # VJOYINTERFACE_API BOOL __cdecl SetDiscPov(int Value, UINT rID, UCHAR nPov);	// Write Value to a given descrete POV defined in the specified VDJ
        # VJOYINTERFACE_API BOOL __cdecl SetContPov(DWORD Value, UINT rID, UCHAR nPov);	// Write Value to a given continuous POV defined in the specified VDJ

        # VJOYINTERFACE_API BOOL		__cdecl	UpdateVJD(UINT rID, PVOID pData); # Update the position data of the specified vJoy Device.

    # VJOYINTERFACE_API BOOL	__cdecl	DriverMatch(WORD * DllVer, WORD * DrvVer);
    def DriverMatch(self):
        verDll = c_short()
        verDrv = c_short()
        self._vjoy.DriverMatch.restype = c_bool
        match = self._vjoy.DriverMatch(byref(verDll), byref(verDrv))
        return match, verDll.value, verDrv.value

    # VJOYINTERFACE_API BOOL	__cdecl	vJoyFfbCap(BOOL * Supported);	// Is this version of vJoy capable of FFB?
    def vJoyFfbCap(self):
        yes = c_bool()
        ok = self._vjoy.vJoyFfbCap(byref(yes))
        if ok:
            return yes.value
        else:
            raise RuntimeError('Calling: vJoyFfbCap failed.')

    # VJOYINTERFACE_API BOOL	__cdecl	GetvJoyMaxDevices(int * n);
    def GetvJoyMaxDevices(self):
        n = c_int()
        ok = self._vjoy.GetvJoyMaxDevices(byref(n))
        if ok:
            return n.value
        else:
            return -1

    # VJOYINTERFACE_API BOOL	__cdecl	GetNumberExistingVJD(int * n);
    def GetNumberExistingVJD(self):
        n = c_int()
        ok = self._vjoy.GetNumberExistingVJD(byref(n))
        if ok:
            return n.value
        else:
            return -1

    # VJOYINTERFACE_API enum VjdStat	__cdecl	GetVJDStatus(UINT rID); // Get the status of the specified vJoy Device.
    def GetVJDStatus(self, rID: int):
        return VjdStat(self._vjoy.GetVJDStatus(rID))


vjoy = VJoy()

if __name__ == '__main__':

    if vjoy.vJoyEnabled():
        print('vJoy is enabled - woohoo!')
        print(f'Version: {vjoy.GetvJoyVersion():04x}')
        print(vjoy.GetvJoyProductString())
        print(vjoy.GetvJoyManufacturerString())
        print(vjoy.GetvJoySerialNumberString())
        print(f'Max devices: {vjoy.GetvJoyMaxDevices()}')
        print(f'Existing devices: {vjoy.GetNumberExistingVJD()}')
        print(f"Force feedback {'is' if vjoy.vJoyFfbCap() else 'is nt'} enabled.")
        match, dllver, drvver = vjoy.DriverMatch()
        if match:
            print(f'DLL Version: {dllver:04x} and Driver Version: {drvver:04x} match.')
        else:
            print(f"DLL Version: {dllver:04x} and Driver Version: {drvver:04x} don't match.")
        print(f'Status: {vjoy.GetVJDStatus(1)}')

        if vjoy.AcquireVJD(1):
            print(f'Status: {vjoy.GetVJDStatus(1)}')
            pressed = False
            for x in (0, 4096, 8192, 16384, 16384+8192, 32768):
                print(x, vjoy.SetAxis(x, 1, HIDUsage.X.value))
                pressed = not pressed
                for button in range(24):
                    vjoy.SetBtn(pressed, 1, button+1)
                time.sleep(2)

            vjoy.RelinquishVJD(1)
            print(f'Status: {vjoy.GetVJDStatus(1)}')
        else:
            print('Could not acquire VJD')

    else:
        print('vJoy is not enabled :-(')
