
import win32api
import win32con
from win32gui import GetWindowText, SetWindowText, GetForegroundWindow, GetWindowRect, EnumWindows
from win32api import GetSystemMetrics




def get_all_windows():
    top_list = []
    window_list = []
    def enum_callback(hwnd, results):
        window_list.append((hwnd, GetWindowText(hwnd)))
    EnumWindows(enum_callback, top_list)


    return window_list






def find_window(window_name):
    #window = [(hwnd, title) for hwnd, title in get_all_windows() if window_name.lower() in title.lower()]
    for hwnd, title in get_all_windows():
        if window_name.lower() == title.lower():
            return (hwnd, title)

    return None



def get_active_window():

    return GetForegroundWindow()

def get_window_name(window_handler):
    return GetWindowText(window_handler)


def set_window_text(window_handler, title):
    SetWindowText(title)

def contains_any(str1, treasure_list):
    for treasure in treasure_list:
        if treasure in str1:
            return True

    return False


def get_window_size(window_handler):
    rect = GetWindowRect(window_handler)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return w,h


#returns top left x,y
def get_window_position(window_handler):
    rect = GetWindowRect(window_handler)
    x = rect[0]
    y = rect[1]
    return x,y


def get_screen_size():
    return GetSystemMetrics(0), GetSystemMetrics(1)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def right_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def get_mouse_position():
    return win32api.GetCursorPos()



def move_mouse(x,y):
    win32api.SetCursorPos((x,y))


# import win32api
# import time
# import math
#
# for i in range(500):
#     x = int(500+math.sin(math.pi*i/100)*500)
#     y = int(500+math.cos(i)*100)
#     win32api.SetCursorPos((x,y))
#     time.sleep(.01)


def click_tab(tab_name):
    tab_offsets = [(-20, -320)]

