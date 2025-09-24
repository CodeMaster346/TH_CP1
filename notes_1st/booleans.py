# TH 2nd Booleans Notes
import time
import datetime as date

over = False

print(over)

name = "Tyler"

print(bool(name))

current_time = time.time()
readable_time = time.ctime(current_time)
print(f"Time: {readable_time}")

now = date.datetime.now()
hour = now.strftime("%H")
month = now.strftime("%m")
day = now.strftime("%d")
year = now.strftime("%y")
# Month = %m %b
# Day = %d
# Year = %Y %y

print(f"Current Time: {now}")
print(f"Hour: {hour}")
print(f"Date: {month}/{day}/{year}")
print(f"My hour variable is a String: {isinstance(hour,str)}")
print(f"My hour variable is a Integer: {isinstance(hour,int)}")
print(f"My hour variable is a Float: {isinstance(hour,float)}")
