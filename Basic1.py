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

 #find area of circle
r = 4
area = 3.14*r**2
print(area)

# first and last name and prints them in reverse order with a space between them
fname ="Rashmi"
lname = "Chaudhary"
print("hello  ", lname ," " ,fname )

# a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
"""variable = input("comma seprated numbers :")
list = variable.split(",")
tuple = tuple(list)
print("list :",repr(list))
print("tuple :",tuple)"""

 #Python program to display the first and last colors from the following list.
list = ["Red","Green","White" ,"Black"]
print(list[0],list[-1])





