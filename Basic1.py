import  sys
import datetime

print("python version")
print(sys.version)
print("version info.")
print(sys.version_info)

#This program for print date and time
now = datetime.datetime.now( )
print("current date and time")
date_time= now.strftime("%Y-%m-%d ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))




