from .ctypes_key import PressKey, ReleaseKey
from bdtime import vk, tt

# press any ch
def down_up(ch, t = 0.5):
    ch = vk.conv_ord(ch)
    PressKey(ch)
    tt.sleep(t)
    ReleaseKey(ch)
    return 1

def main():
    # KeyDown and KeyUp
    ch = 'a'
    tt.sleep(1)
    down_up(ch)

    # select all
    tt.sleep(1)
    PressKey(vk.ctrl)
    PressKey(vk.a)
    tt.sleep(0.5)
    ReleaseKey(vk.a)
    ReleaseKey(vk.ctrl)

    return 1


if __name__ == '__main__':
    main()