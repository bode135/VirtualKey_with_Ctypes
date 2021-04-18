from .ctypes_key import PressKey, ReleaseKey
from bdtime import vk, tt

# press any ch
def down_up(ch, t = 0.5):
    ch = vk.conv_ord(ch)
    PressKey(ch)
    tt.sleep(t)
    ReleaseKey(ch)


if __name__ == '__main__':
    main()