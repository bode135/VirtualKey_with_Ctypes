from ctypes import POINTER, c_ulong, Structure, c_ushort, c_short, c_long, byref, windll, pointer, sizeof, Union
from bdtime import tt, vk
import keyboard
import win32con


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

def sendkey(scancode, pressed=1):
    """
    Reference:
    [MOUSEINPUT structure (winuser.h)]
    (https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput)
    [scancodes](https://www.win.tue.nl/~aeb/linux/kbd/scancodes-1.html)

    :param scancode: 扫描码, 若为tuple, 则取第一个.
    :param pressed:
    :return:
    """
    if isinstance(scancode, tuple):
        scancode = scancode[0]      # 若按键有两个扫描码, 类型: tuple; 则取第一个扫描码 .

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
    # windll.user32.GetAsyncKeyState(scancodes.get('alt')[0])
    # scancodes.get('q')
    # windll.user32.GetAsyncKeyState(vk.q)
    #
    # for i in range(10):
    #     tt.sleep(1)
    #     if tt.stop():
    #         break
    #     print(windll.user32.GetAsyncKeyState(vk.q))

    windll.user32.SendInput(1, pointer(InputBox), sizeof(InputBox[0]))
    return 1


class scancodes:
    @classmethod
    def get(self, key):
        # 一个字符一般对应两个扫描码
        return keyboard.key_to_scan_codes(key)

    @classmethod
    def ret_one_scancode(self, key):
        # 只返回一个
        return keyboard.key_to_scan_codes(key)[0]

def scancode_down_up(key, t=0.5):
    # 基于扫描码: ScanCodes, scancodes类
    return sendkey(scancode=scancodes.get(key))


def keybd_event(ch, t=0.1):
    # 基于虚拟按键码: VirtualKeyCodes, vk类
    ret = windll.user32.keybd_event(
        vk.conv_ord(ch),
        scancodes.get(ch)[0],
        win32con.KEYEVENTF_EXTENDEDKEY | 0,
        0,
    )
    return ret



if __name__ == '__main__':
    # tt.sleep(1)
    # move_click(get_mpos())
    # tt.sleep(1)
    # move_right_click(get_mpos())
    #
    # def hex_to_dec(int_hex):
    #     if (isinstance(int_hex, (int, float))):
    #         int_hex = str(int_hex)
    #     int_dec = int(int_hex, 16)
    #     return int_dec
    tt.sleep(1)
    scancode_down_up('a')

    tt.sleep(0.1)
    keybd_event('a')


    # @tt.run_f_with_during(5, 1)
    # def f():
    #     sendkey(scancode=scancodes.get('e'))
    #     tt.sleep(0.01)
    #     sendkey(scancode=scancodes.get('w'))
    #     tt.sleep(0.01)
    #     sendkey(scancode=scancodes.get('q'))
    # f()
    #
    # tt.sleep(1)
    # windll.user32.keybd_event(vk.q, scancodes.get('q')[0])
    # tt.sleep(1)
    # windll.user32.keybd_event(vk.q, scancodes.get('w')[0])
    # tt.sleep(1)
    # windll.user32.keybd_event(vk.q, scancodes.get('e')[0])
    #
    # tt.sleep(1)
    # windll.user32.keybd_event(2, scancodes.get(''))

