Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import psutil
from plyer import notification
import time

def conversion(sec): #function to convert seconds into Hr and min
    sec_value = sec % (24*3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    min_value = sec_value // 60
    return hour_value,min_value

while True:
    battery = psutil.sensors_battery()
    h,m=conversion(battery.secsleft)
    notifcation.notify(
        title="Battery Percentage ",
        message = f'{h}Hr {m}Min {battery.percent}% remaining' ,
        timeout =10
        )
time.sleep(60.60)
