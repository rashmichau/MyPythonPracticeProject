import sys
import datetime

# print("python version")
# print(sys.version)
# print("version info.")
# print(sys.version_info)
#
# # This program for print date and time
# now = datetime.datetime.now()
# print("current date and time")
# date_time = now.strftime("%Y-%m-%d ")
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
#
# # find area of circle
# r = 4
# area = 3.14 * r ** 2
# print(area)
#
# # first and last name and prints them in reverse order with a space between them
# fname = "Rashmi"
# lname = "Chaudhary"
# print("hello  ", lname, " ", fname)
#
# # a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# """variable = input("comma seprated numbers :")
# list = variable.split(",")
# tuple = tuple(list)
# print("list :",repr(list))
# print("tuple :",tuple)"""
#
# # Python program to display the first and last colors from the following list.
# list = ["Red", "Green", "White", "Black"]
# print(list[0], list[-1])
#
# # Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# Examdate = 2, 5, 2024
# print("the examination shedule :%i/ %i / %i" % Examdate)
#
# # # program that accepts an integer (n) and computes the value of n+nn+nnn.
# # a = int(input("enter the value :"))
# # n1 = int("%s" % a)
# # n2 = int("%s%s" % (a, a))
# # n3 = int("%s%s%s" % (a, a, a))
# # print(n1 + n1 + n3)
#
# # printthedocuments(syntax, descriptionetc.) ofPythonbuilt - in function(s).
# print(abs.__doc__)
#
# # Write a Python program to get the volume of a sphere with radius six.
# from math import pi
#
# r = 6
# vsph = float(4 / 3 * pi * (r ** 3))
# print("volume of sphere:", vsph)

# Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice theabsolute difference.
# a = int(input("any no:"))
# b = 17
# if a > 17:
#     print("no is grater than 17 :", 2 * (a - b))
# elif a == 17:
#     print("not greater nor smaller", -(a - b))
# else:
#     print("no is smaller than 17 :",- (a - b))

#program to test whether a not number is within 100 of 1000 or 2000
a=int(input("any number:"))
if a<=1100 and a>=900 in range(1100):
    print('number within 100 of 1000 ')
elif a<=2100 and a>=1900 in range (2000,) :
    print('number  within 100 of 2000')
else :
    print("no is not in range of 1000 or 2000")

