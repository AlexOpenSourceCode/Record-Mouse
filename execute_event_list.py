import win32api, win32con, time, win32ui, pyHook, pythoncom
import win32gui
import multiprocessing
from multiprocessing import Process, Value, Array, freeze_support, Manager
import pythoncom, pyHook
import random

from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect
from win32api import GetSystemMetrics


import os



event_list = [(979, 558, 'right'), 0.9550001621246338, (941, 600, 'left'), 2.815000057220459, (710, 511, 'right'), 0.8029999732971191, (702, 614, 'left'), 2.8529999256134033, (1060, 65, 'left'), 1.2850000858306885, (1737, 766, 'left'), 2.3939998149871826, (385, 353, 'left'), 19.59500002861023, (1781, 873, 'left'), 1.2920000553131104, (1820, 875, 'left'), 2.4579999446868896, (254, 954, 'right'), 0.8860001564025879, (234, 1017, 'left'), 19.39299988746643, (1734, 765, 'left'), 3.005000114440918, (909, 482, 'left'), 11.38699984550476, (1888, 157, 'left'), 9.374000072479248, (1122, 645, 'right'), 2.0409998893737793, (1049, 686, 'left'), 2.9509999752044678, (1820, 878, 'right'), 1.8000001907348633, (1810, 977, 'left'), 3.248999834060669, (708, 507, 'right'), 1.6770000457763672, (677, 607, 'left'), 1.6159999370574951, (1061, 67, 'left'), 1.0190000534057617, (1774, 872, 'left'), 0.5069999694824219, (1818, 876, 'left'), 2.4020001888275146, (254, 947, 'right'), 1.11899995803833, (241, 1011, 'left'), 18.786999940872192, (974, 549, 'right'), 1.3940000534057617, (900, 592, 'left'), 1.250999927520752, (1823, 874, 'right'), 1.2190001010894775, (1791, 973, 'left'), 2.3420000076293945, (1061, 64, 'left')]


repeat = True


import traceback
def OnKeyboardEvent(event):
    global repeat
    print "KEYBOARD EVENT"
    try:
        if event.Key == 'S' or event.Key == 's':
            repeat = False
            print "EXITING"
            os._exit(1)

        print event.Key
    except:
        print "EXITING"
        print traceback.print_exc()
        os._exit(1)

    return True



def pywinauto_click(x,y,mouse_button):
    import pywinauto.application

    app = pywinauto.application.Application()
    comapp = app.connect_(path = "explorer")

    for i in comapp.windows_():
        if "Progman" == i.FriendlyClassName():
            #i.MoveMouse(coords=(x + 1920, y))
            i.ClickInput(coords=(x + 1920, y), button=mouse_button)
            #i.ClickInput(coords=(x, y))

import time, math


def distance(x1, y1, x2, y2):
    val_ = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
    d = math.sqrt(val_)
    return d

def smooth_move_mouse_to_position(target_x,target_y):
    win32api.SetCursorPos((target_x, target_y))
    time.sleep(0.1)


def click_2(x,y,mouse_button):


    #win32api.SetCursorPos((x,y))
    smooth_move_mouse_to_position(x,y)
    time.sleep(0.2)
    if mouse_button == 'left':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    elif mouse_button == 'right':
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)




def generate_random_float(low_f, high_f):
    return random.uniform(low_f,high_f)


def contains_any(str1, treasure_list):
    for treasure in treasure_list:
        if treasure in str1:
            return True

    return False

def execute_actions_handler():
    global repeat
    global event_list
    time_inbetween_actions = 5

    count = 0
    while repeat:
        #time_inbetween_actions = generate_random_float(10, 25)

        p = Process(target=execute_actions, args=())
        p.start()
        p.join()

        count += 1



def window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

def get_app_list(handles=[]):
    mlst=[]
    win32gui.EnumWindows(window_enum_handler, handles)
    for handle in handles:
        mlst.append(handle)
    return mlst



def get_mouse_position():
    return win32api.GetCursorPos()

z = 0
def execute_actions():
    global z

    for event in event_list:

        active_window = get_active_window()
        active_window_name = get_window_name(active_window)

        print "active window name: " + active_window_name

        while not contains_any(active_window_name,['OSBuddy', 'RS', 'runescape', 'RuneScape']):
            print "Not runescape window, sleeping"
            time.sleep(5)

            active_window = get_active_window()
            active_window_name = get_window_name(active_window)

        if type(event) == type((1,2,'sss')):
            click_2(event[0], event[1], event[2])

            z += 1
            print z
        elif type(event) == type(1.11):
            time.sleep(event)
        else:
            ran_sleep_time = event + generate_random_float(event * (-.1), event * .1)
            print "original sleep"
            print event
            print 'random sleep time'
            print ran_sleep_time


            time.sleep(ran_sleep_time)

execute_actions()


if __name__ == '__main__':

    multiprocessing.freeze_support()

    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()


    p = Process(target=execute_actions_handler, args=())
    p.start()

    try:
        pythoncom.PumpMessages()   #This call will block forever unless interrupted
    except (KeyboardInterrupt, SystemExit) as e: #We will exit cleanly if we are told
        print(e)


        os._exit(1)





