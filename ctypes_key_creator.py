from ctypes import POINTER, c_ulong, Structure, c_ushort, c_short, c_long, byref, windll, pointer, sizeof, Union
from bdtime import tt, vk

PUL = POINTER(c_ulong)


class KeyBdInput(Structure):
    _fields_ = [("wVk", c_ushort),
                ("wScan", c_ushort),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(Structure):
    _fields_ = [("uMsg", c_ulong),
                ("wParamL", c_short),
                ("wParamH", c_ushort)]


class MouseInput(Structure):
    _fields_ = [("dx", c_long),
                ("dy", c_long),
                ("mouseData", c_ulong),
                ("dwFlags", c_ulong),
                ("time", c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(Structure):
    _fields_ = [("type", c_ulong),
                ("ii", Input_I)]


class POINT(Structure):
    _fields_ = [("x", c_ulong),
                ("y", c_ulong)]


def get_mpos():
    orig = POINT()
    windll.user32.GetCursorPos(byref(orig))
    return int(orig.x), int(orig.y)


def set_mpos(pos):
    x, y = pos
    windll.user32.SetCursorPos(x, y)


MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

MOUSEEVENTF_RIGHTDOWN = 0x00008
MOUSEEVENTF_RIGHTUP = 0x0010


def move_click(pos, move_back=False):
    origx, origy = get_mpos()
    set_mpos(pos)
    FInputs = Input * 2
    extra = c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, 2, 0, pointer(extra))

    tt.sleep(0.1)

    ii2_ = Input_I()
    ii2_.mi = MouseInput(0, 0, 0, 4, 0, pointer(extra))
    x = FInputs((0, ii_), (0, ii2_))
    windll.user32.SendInput(2, pointer(x), sizeof(x[0]))
    if move_back:
        set_mpos((origx, origy))
        return origx, origy

def move_right_click(pos, move_back=False):
    origx, origy = get_mpos()
    set_mpos(pos)
    FInputs = Input * 2
    extra = c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, MOUSEEVENTF_RIGHTDOWN, 0, pointer(extra))

    tt.sleep(0.1)

    ii2_ = Input_I()
    ii2_.mi = MouseInput(0, 0, 0, MOUSEEVENTF_RIGHTUP, 0, pointer(extra))
    x = FInputs((0, ii_), (0, ii2_))
    windll.user32.SendInput(2, pointer(x), sizeof(x[0]))
    if move_back:
        set_mpos((origx, origy))
        return origx, origy

def sendkey(scancode, pressed):
    FInputs = Input * 1
    extra = c_ulong(0)
    ii_ = Input_I()
    flag = 0x8
    ii_.ki = KeyBdInput(0, 0, flag, 0, pointer(extra))
    InputBox = FInputs((1, ii_))
    if scancode is None:
        return
    InputBox[0].ii.ki.wScan = scancode
    InputBox[0].ii.ki.dwFlags = 0x8

    if not (pressed):
        InputBox[0].ii.ki.dwFlags |= 0x2

    windll.user32.SendInput(1, pointer(InputBox), sizeof(InputBox[0]))

if __name__ == '__main__':

    tt.sleep(1)
    move_click(get_mpos())
    tt.sleep(1)
    move_right_click(get_mpos())

    def hex_to_dec(int_hex):
        if(isinstance(int_hex, (int, float))):
            int_hex = str(int_hex)
        int_dec = int(int_hex, 16)
        return int_dec

    class ScanCode:
        q = hex_to_dec(10)
        w = hex_to_dec(11)
        e = hex_to_dec(12)
        r = hex_to_dec(13)
        pass

    from keyboard import *

    sc = ScanCode()

    tt.sleep(1)
    sendkey(scancode=sc.e, pressed=1)

    # Using Keyboard module in Python
    import keyboard

    # It writes the content to output
    keyboard.write("GEEKS FOR GEEKS\n")

    # It writes the keys r, k and endofline
    keyboard.press_and_release('shift + r, shift + k, \n')
    keyboard.press_and_release('R, K')

    # it blocks until ctrl is pressed
    keyboard.wait('Ctrl')