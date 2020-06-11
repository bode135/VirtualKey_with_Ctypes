# Next up is the Virtual Key Code.
````
class VK:
    ms_l = mouse_left = vk_lbutton = VK_LBUTTON = 1
    ms_r = mouse_right = vk_rbutton = VK_RBUTTON = 2
    cancel = VK_CANCEL = 3
    ms_m = mouse_middle = vk_mbutton = VK_MBUTTON = 4

    vk_xbutton1 = VK_XBUTTON1 = 5
    vk_xbutton2 = VK_XBUTTON2 = 6



    backspace = 8
    tab = 9
    clear = 12
    # enter = 13
    # shift = 16
    # ctrl = 17
    # alt = 18
    pause = 19
    caps_lock = 20
    esc = 27
    spacebar = 32
    page_up = 33
    page_down = 34
    end = 35
    home = 36
    left_arrow = 37
    up_arrow = 38
    right_arrow = 39
    down_arrow = 40
    select = 41
    print = 42
    execute = 43
    print_screen = 44
    insert = 45
    delete = 46
    help = 47
    num_0 = 48      # keyboard virtual key code
    num_1 = 49
    num_2 = 50
    num_3 = 51
    num_4 = 52
    num_5 = 53
    num_6 = 54
    num_7 = 55
    num_8 = 56
    num_9 = 57
    a = 65
    b = 66
    c = 67
    d = 68
    e = 69
    f = 70
    g = 71
    h = 72
    i = 73
    j = 74
    k = 75
    l = 76
    m = 77
    n = 78
    o = 79
    p = 80
    q = 81
    r = 82
    s = 83
    t = 84
    u = 85
    v = 86
    w = 87
    x = 88
    y = 89
    z = 90
    numpad_0 = 96       # keypad virtual key code
    numpad_1 = 97
    numpad_2 = 98
    numpad_3 = 99
    numpad_4 = 100
    numpad_5 = 101
    numpad_6 = 102
    numpad_7 = 103
    numpad_8 = 104
    numpad_9 = 105
    multiply_key = 106
    add_key = 107
    separator_key = 108
    subtract_key = 109
    decimal_key = 110
    divide_key = 111
    F1 = 112
    F2 = 113
    F3 = 114
    F4 = 115
    F5 = 116
    F6 = 117
    F7 = 118
    F8 = 119
    F9 = 120
    F10 = 121
    F11 = 122
    F12 = 123
    F13 = 124
    F14 = 125
    F15 = 126
    F16 = 127
    F17 = 128
    F18 = 129
    F19 = 130
    F20 = 131
    F21 = 132
    F22 = 133
    F23 = 134
    F24 = 135
    num_lock = 144
    scroll_lock = 145
    left_shift = 160
    right_shift = 161
    left_control = 162
    right_control = 163
    left_menu = 164
    right_menu = 165
    browser_back = 166
    browser_forward = 167
    browser_refresh = 168
    browser_stop = 169
    browser_search = 170
    browser_favorites = 171
    browser_start_and_home = 172
    volume_mute = 173
    volume_Down = 174
    volume_up = 175
    next_track = 176
    previous_track = 177
    stop_media = 178
    play = 179
    pause_media = 179
    start_mail = 180
    select_media = 181
    start_application_1 = 182
    start_application_2 = 183
    attn_key = 246
    crsel_key = 247
    exsel_key = 248
    play_key = 250
    zoom_key = 251
    clear_key = 254

    symbol = {'+': 0xBB,
               ',': 0xBC,
               '-': 0xBD,
               '.': 0xBE,
               '/': 0xBF,
               '`': 0xC0,
               ';': 0xBA,
               '[': 0xDB,
               '\\': 0xDC,
               ']': 0xDD,
               "'": 0xDE,
               '\`': 0xC0}

    Constant = 8000 # signal
    Time = 0.5


    # hot key
    shift = 16
    ctrl = 17
    alt = 18

    f1 = 112
    f2 = 113
    f3 = 114
    f4 = 116
    f5 = 117

    enter = 13
    space = 32
    back = 8

    # keypad
    n0, n1, n2, n3, n4, n5, n6, n7, n8, n9 = 96, 97, 98, 99, 100, 101, 102, 103, 104, 105
    left, up, right, down = 37, 38, 39, 40

    def conv_ord(self, ch):     # convert data type, return: vitual_key_code
        # ch = 'q'
        if isinstance(ch, int):
            return ch
        if isinstance(ch, str):
            if ch.islower():
                ch = ch.upper()
            return ord(ch)

    1
vk = VK()
````
# So you can use it like this way:<br/>
````

from ctypes_key import PressKey, ReleaseKey
from my_time import vk
import time as tt

# press any ch
def down_up(ch, t = 0.5):
    ch = vk.conv_ord(ch)
    PressKey(ch)
    tt.sleep(t)
    ReleaseKey(ch)

def main():
    ch = 'a'        # KeyDown and KeyUp
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

````