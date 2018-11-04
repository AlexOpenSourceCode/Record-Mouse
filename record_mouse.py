import win32api, win32con, time, win32ui, pyHook, pythoncom

import datetime
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)





current_milli_time = lambda: int(round(time.time() * 1000))

current_time_seconds = lambda: time.time()

event_list = []

last_time_seconds = current_time_seconds()

def onclick(event):

    print event
    print dir(event)
    print event.Message
    print event.GetMessageName


    return True

#(x,y,'left') or (x,y,'right')
def add_click_list_event(click_list_event):

    global last_time_seconds

    if len(event_list) == 0:
        event_list.append(click_list_event)
    else:
        event_list.append(current_time_seconds() - last_time_seconds)
        event_list.append(click_list_event)

    last_time_seconds = current_time_seconds()


    print event_list



def left_down(event):
    event_tuple = event.Position + ('left',)
    add_click_list_event(event_tuple)
    return True

def right_down(event):
    event_tuple = event.Position + ('right',)
    add_click_list_event(event_tuple)
    return True

def middle_down(event):
    global click
    click = 0
    print(click)
    return True

hm = pyHook.HookManager()
hm.SubscribeMouseLeftDown(left_down)
hm.SubscribeMouseRightDown(right_down)
hm.SubscribeMouseMiddleDown(middle_down)
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()

