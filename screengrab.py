import pyautogui
import keyboard
import os
import datetime
import getpass
# import win10toast
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()

username = getpass.getuser()
myScreenshot = pyautogui.screenshot()

folder_selected=f"C:/Users/{username}/Documents/"
name="S6"
path = os.path.join(folder_selected,name)
try:
    os.mkdir(path)
except:
    None
x = datetime.datetime.now()
day=x.strftime("%d %B (%a)")

try:
    date_folder= os.path.join(path, day)
    os.mkdir(date_folder)
except:
     None

def screenshot(path1,name):
    n.show_toast("SCREEN GRAB", name, duration=3)
    nameing=f"{path1}/{name}.png"
    myScreenshot.save(nameing)



def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

def dir_build(date_folder,time_name):
    try:
        time_folder = os.path.join(date_folder,time_name)
        os.mkdir(time_folder)
    except:
        None
    return time_folder

def start():
    timeNow = datetime.datetime.now()
    time_str=timeNow.strftime('%I-%M-%S %m-%d-%Y')
    if timeNow < todayAt (10,10) and timeNow> todayAt(9):
        time_name_1="1st period"
        time_path=dir_build(date_folder,time_name_1)
        screenshot(time_path, time_str)

    elif timeNow < todayAt (11,20) and timeNow> todayAt(10,10):
        time_name_2 = "2nd period"
        time_path=dir_build(date_folder, time_name_2)
        screenshot(time_path, time_str)

    elif timeNow < todayAt (12,30) and timeNow> todayAt(11,20):
        time_name_3 = "3rd period"
        time_path=dir_build(date_folder, time_name_3)
        screenshot(time_path, time_str)

    elif timeNow < todayAt (13,40) and timeNow> todayAt(12,30):
        time_name_4 = "4th period"
        time_path=dir_build(date_folder, time_name_4)
        screenshot(time_path, time_str)
    elif timeNow < todayAt (16,10) and timeNow> todayAt(13,40):
        time_name_aft= "After_noon p"
        time_path=dir_build(date_folder, time_name_aft)
        screenshot(time_path, time_str)
    else:
        time_name_oth= "Other"
        time_path=dir_build(date_folder, time_name_oth)
        screenshot(time_path,time_str)


start()

