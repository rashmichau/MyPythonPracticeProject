#exponential que
# num=int(input("enter any num :"))
# result=num**(0.5)
# print(result)

#type two
# import math
# num=int(input("enter any num :"))
# result=math.sqrt(num)
# print(result)

#area of triangle
# height =float(input("enter value :"))
# base =float(input("enter value :"))
# area = (1/2)*base*height
# print(area)

#swap two variable
# a,b=12,13
# a,b=b,a
# print(a,b)
#type 2
# a,b=23,34
# exc=a
# a=b
# b=exc
# print(a,b)

#convert kilometers into miles
# km=float(input("enter kilometers :"))
# miles=(0.621371)*km
# print(km,"km in miles is ",miles)

#num is positive,negative or zero
# num =int(input("enter any num :"))
# if num>0:
#     print("num is positive")
# elif num==0:
#     print("num is zero")
# else:
#     print("num is negative ")

#number is odd or even
# num =int(input("enter num :"))
# if num%2==0:
#     print("number is even")
# else:
#     print("num is odd")

#check leap year
# year =int(input("enter any year :"))
# if year%400==0 and year%100==0 :
#     print(year,"is a leap year")
# elif year%4==0 and year%100!=0 :
#     print(year,"is a leap year")
# else :
#     print(year,"is not a leap year")

#largest in three nums
# a=int(input("enter any year :"))
# b=int(input("enter any year :"))
# c=int(input("enter any year :"))
# if a>b and a>c :
#     print("the greater num is ",a)
# elif b>c and b>a :
#     print("the greater num is ",b)
# else:
#     print("the greater num is ",c)

# check prime num
# num =int(input("enter any num :"))
# count=0
# i=1
# while(i<=num):
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("it is a prime num")
# else:
#     print("it is not a prime num")
# type 2
# num =int(input("enter the num :"))
# if num==1:
#     print("num is not prime")
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("num is not prime")
#             break
#     else:
#         print("num is prime")

# generate random num
# from random import randint
# for i in range(11):
#     print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')

#print all prime num
# start_digit=int(input("enter any num :"))
# end_digit=int(input("enter any num :"))
# print("prime numbers b/w num is :")
# for num in range(start_digit,end_digit):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

#factorial of number
# num = int(input("enter any num for fact :"))
# factor =1
# if num<0:
#     print("not defined factorial for this num")
# if num==0:
#     print("factorial of zero is always one")
# if num>0:
#     for i in range(1,num+1):
#         factor*=i
# print("the factorial of num is : ",factor)

#display the multiplication table
# num = int(input("enter any num :"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

#fibonacci series
# num=int(input("enter num :"))
# a=0
# b=1
# c=0
# while(c<=num):
#     print(c)
#     a=b
#     b=c
#     c=a+b

# check number is armstrong or not
# num = int(input("enter number :"))
# order = len(str(num))
# sum =0
# digit=num
# while (digit>0):
#     temp=digit%10
#     cube=temp**order
#     sum=sum+cube
#     digit=digit//10
# if sum==num :
#     print("it is a armstrong num")
# else:
#     print("it is not a armstrong num")

#armstrong number in an interval
# lower=int(input("enter start num :"))
# upper=int(input("enter last num :"))
# for num in range(lower,upper):
#     order=len(str(num))
#     sum =0
#     temp=num
#     while (temp>0):
#         digit=temp%10
#         sum+=digit**order
#         temp//=10
#     if sum==num:
#         print(sum)

#sum of natural numbers
# n=int(input("enter any num :"))
# if n>0:
#     sum=0
#     for num in range(0,n+1):
#         sum=sum+num
#     print(sum)
# else:
#     print("not natural number")

#display power of two using anonymous function
# terms=int(input("enter the terms :"))
# result= list(map(lambda x : 2**x ,range(terms+1)))
# print(result)
# for i in range(terms+1):
#     print("the power of 2 is",i,"resulting",result[i])

#the number divisible by another num
# num =int(input("enter the num :"))
# print("the num b/w 1 to 100 is divisible by",num,"is -")
# for i in range(1,100+1):
#     if i%num==0:
#         print(i)
#type 2
# num=int(input("enter the num for divide :"))
# rang =int(input("enter the range num :"))
# result=list(filter(lambda x:x%num==0,range(rang+1)))
# print(result)

#conver decimal to binary,octal and hexadecimal
# decimal=int(input("enter the decimal num :"))
# print("the conversion of ",decimal,"number to")
# print("binary num is",bin(decimal))
# print("octal num is ",oct(decimal))
# print("hexadecimal is ",hex(decimal))

#Find ASCII value of character program:
# char = 'Z'
# print("the value of",char,"is :",ord(char))

#find hcf or gcd in two nums in python
# def find_hcf(x,y):
#     if x>y:
#         smaller=y
#     else:
#         smaller=x
#     for i in range(1,smaller+1):
#         if x%i==0 and y%i==0:
#             hcf=i
#     return hcf
# x=int(input("enter num 1 :"))
# y=int(input("enter num 2 :"))
# print("the hcf of two num is :",find_hcf(x,y))

# Find the factors of a num
# num=int(input("enter any num :"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i)

#program for mini calculator
# print("~~~~~~~~MINI CALCULATOR~~~~~~~~~")
# num1 = float(input("enter valur 2 :"))
# print("choose value 1 for addition \n choose value 2 for subtraction \n choose value 3 for multiplication \n choose value 4 for division")
# choice = int(input("your choice 1 :"))
# num2 = float(input("enter choice value :"))
# if choice==1:
#     print("the addition is =",num1+num2)
# elif choice==2:
#     print("the subtraction is =",num1-num2)
# elif choice==3:
#     print("the multiplication is =",num1*num2)
# elif choice==4:
#     print("the division is =",num1/num2)
# else:
#     print("invalid input")

#Program to shuffle deck of cards
# import random, itertools
# deck = list(itertools.product(range(1, 14), ["spade", "hearts", "club", "dimond"]))
# random.shuffle(deck)
# print(deck)
# for i in range(4):
#     print(deck[i] [0], "of", deck[i] [1])

# Display calendar of month in year
# import calendar
# year = int(input("enter the year :"))
# month = int(input("enter the month :"))
# calendar = calendar.month(year,month)
# print(calendar)

# Fibonacci sequence by recursion function
# def fibo(n): # n is a term of fibonacci series
#     if n<=1:
#         return n
#     else:
#         return (fibo(n-1)+fibo(n-2))
# n = int(input("enter number :"))
# if n<=0:
#     print("please enter positive num ")
# else:
#     print("fibonacci terms is")
#     for i in range(n):
#         print(fibo(i))

#find the sum of natural numbers using recursion function
# def SNN (n):
#     if n==1:
#         return 1
#     else:
#         return  n+SNN(n-1)
# n = int(input("enter the number 1 to --"))
# if n<=0:
#     print("please put positive integers ")
# else:
#     print("sum of natural numbers is :",SNN(n))

#find factorial using recursion function
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter num for factorial :"))
# if n<0:
#     print("please put positive numbers")
# else:
#     print("the factorial of",n,"is",fact(n))

#conver binary to decimal using recursion
# def convertbinary(n):
#     if n>1:
#         convertbinary(n//2 )
#         print(n%2,end="")
# n= int(input("enter any decimal number :"))
# convertbinary(n)

#addition of two matrix
# A =[[ 2, 7, 8],
#    [ 6, 8, 9],
#    [15,23,19]]
# B =[[10, 6, 9],
#    [ 6, 8, 5],
#    [9, 12,13]]
# result =[[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[i][j] =A[i][j]+B[i][j]
# for r in result :
#     print(r)

#transpose of a matrix
# A = [[2,3,4],
#      [5,6,7]]
# Trans =[[0,0],
#         [0,0],
#         [0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         Trans[j][i] = A[i][j]
# for r in Trans:
#     print(r)
# #Type 2
# print("this is the second type of transpose")
# A = [[2,3,4],
#      [5,6,7]]
# T =[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
# for i in T:
#     print(i)

#string is palindrome or not
# string = input("Enter any string :")
# result =string[ : :-1]
# print(result)
# if string==result:
#     print("Yes string is palindrome ")
# else:
#     print("string is not palindrome")
#
# #Remove punctuation from string
# punc ='''~!@#:$%^&*()_-"={}.,[]\;></?'''
# string =input("Enter any string :")
# empty_str = ""
# for i in string:
#     if i not in punc:
#         empty_str +=i
# print(empty_str)

#multiplication of two matrices
# A =[[1,2,3],
#    [4,5,6],
#    [7,8,9]]
# B =[[1,3,5],
#    [4,6,8],
#    [7,8,9]]
# result =[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A[0])):
#         result[i][j]=A[i][j]*B[i][j]
# for r in result:
#     print(r)

# Program to sort words in alphabetic order
# a = "Python language Is generated In 1991 by Gudio Van Rossum"
# w = a.split()
# for i in range(len(w)):
#     w[i]=w[i].lower()
# print(w)
# w.sort()
# print(w)

#program to illustrate different set operation
# A = {1,2,3,4,8,9}
# B = {7,8,4,3,5}
# print("the set of union operation is :",A|B)
# print("the set of intersection operation is :",A&B)
# print("the set of difference operation is :",A-B)
# print("the symmetric difference operation is :",A^B)

#Count the number of vowels in string
# a =input("enter any sentence :")
# vowel="aeiou"
# a=a.casefold()
# print(a)
# count={}.fromkeys(vowel,0)
# for i in a:
#     if i in vowel:
#         count[i] +=1
# print(count)
#Type 2
# count={key:sum ([1 for char in a if char==key])for key in vowel}
# print(count)

#How to merge two dictionary
# dict1 = {"devu":26,"devyani":27}
# dict2 = {"soniya":38,"devu":39}
# print(dict1|dict2)
# #type 2 using quark
# print({**dict1,**dict2})
# # type 3 if we want first value
# dict3=dict2.copy()
# dict3.update(dict1)
#print(dict3)

# indexing of list using for loop (by enumerate method)
# list =[34,56,78,9,3]
# for index,value in enumerate(list):
#     print(index,value)
# #(type 2)
# for index in range(len(list)):
#     value =list[index]
#     print(index,value)

#slicing on list in python
# l = ["Rashmi","yogesh","husband","wife","love","relationship"]
# print(l[0:6])
# print(l[3:4])
# print(l[ : :-1])
# print(l[-6:6])
# print(l[ : ])

#itrate over dictionary using for loop
# friends ={"computer":"programing","python":"language","java":"coding lang"}
# for key,value in friends.items():
#     print(key,":",value)
# #type 2
# for key in friends:
#     print(key,":",friends[key])
# #type 3- keys,value separation
# for key in friends.keys():
#     print(key)
# for value in friends.values():
#     print(value)

# sort dictionary by values
# marks = {"renu":23,"vidya":33,"rahul":45,"mahak":49}
# sv = sorted(marks.items(),key=lambda x: x[1])
# print(sv)
# #type 2
# st=sorted(marks.values())
# print(st)
# stv =sorted(marks.keys())
# print(stv)
# tot=sorted(marks.items())
# print(tot )

#check if a list is empty
# my_list = [2,3,4]
# if not my_list:
#     print("list is empty")
# #type 2
# if my_list==[]:
#     print("list is empty")
# if len(my_list)==0:
#     print("list is empty")
# else:
#     print("your list is filled with your nums")

#catch multipal exception handling
# string = input("enter any string :")
# num = int(input("enter any num :"))
# try:
#     total = (string+num)
#     print(total)
# except (ValueError,TypeError ) as a:
#     print(a)
# print("you nailed it")

#copy one file content to another file
# from shutil import copyfile
# copyfile(C:/Users/Rashmi/OneDrive/Desktop/doc yogirashu/Yogesh_9yrExp_Android,C:/Users/Rashmi/OneDrive/Desktop/doc yogirashu/YogeshChaudhary_cover)

#concinate two list using methods of python
# l1=[1,3,7,9,"a","f","g"]
# l2=[5,8,7,3,4,"c","j","f"]
# l12 = l1+l2
# print(l12)
# #type 2 -unique values
# l3 = list(set(l1+l2))
# print(l3)
# # type 3 - by extend method
# l1.extend(l2)
# print(l1)

#check if key is present in dictionary
# friends = {"soni":"khushi","devu":"varshu","devyani":"alone"}
# name = input("enter any name present as key :")
# if name in friends.keys():
#     print("yes",name," as key is present in dict")
# else:
#     print("please enter some useful stuff")

#parse a string into float or integer
# string = "3456.87"
# print(type(string))
# string_float = float(string)
# print(type(string_float))
# string_int = int(float(string))
# print(type(string_int))

#convert string to datetime module
# from datetime import datetime
# string = "oct 14 1997 7:30AM"
# datetime = datetime.strptime(string,"%b %d %Y %I:%M%p" )
# print(datetime)
# print(type(datetime))

#program to get the last element of list
# list =[34,76,98,77,55,69]
# print(list[-1])
#
# #program to get a sub string of string
# string = input("enter any string :")
# substr = input("enter substring of string :")
# if substr in string :
#     print("yes substring is present in string")
# else:
#     print(" substring is not present in string")

#print output without a new line
# print("rashmi chaudhary",end=" ")
# print("is a python developer also.")

#check if a string is a valid keyword or not
# import keyword
# words = ["break","continue","john","for","while","in"]
# for i in range(len(words)):
#     if keyword.iskeyword(words[i]):
#         print(words[i],"is a keyword in python")
#     else:
#         print(words[i],"is not keyword in python")

#1. reverse a list without using reverse keyword
# list = [1,2,3,4,5]
# print(list[ : :-1])

#sum of all element of list
# list =[10,20,30,40]
# sum=0
# for i in range(len(list)):
#     sum=sum+list[i]
# print(sum)

#find the largest and smallest number in list
# list=[5,2,9,1,7]
# maximum =max(list)
# print("maximum",maximum)
# minimum =min(list)
# print("minimum",minimum)

#check if list contains duplicate
# lis1 =[1,2,3,4,2]
# lis2 =list(set(lis1))
# if lis1!=lis2:
#     print("list have duplicate items")
# else:
#     print("list have not duplicate items")

#merge two list without duplicate
# l1 =[1,2,3]
# l2 =[3,4,5]
# l3=l1+l2
# print(list(set(l3)))

#find second large element in list
# l=[4,1,7,3,9]
# m =max(l)
# print("first maximum no is",m)
# l.remove(m)
# m2=max(l)
# print("second maximum no is",m2)

#remove all even nums from list
# l =[1,2,3,4,5,6]
# for i in (l) :
#     if i%2==0:
#         l.remove(i)
# print(l)

#intersection of two list
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# l3 = list(set(l1)&set(l2))
# print(l3)

#write a program to find a missing num
# def find_missing(lst):
#     return sorted(set(range(lst[0],lst[-1]))-set(lst))
# lst=[1,2,4,5,6]
# print(find_missing(lst))

#count the specific element in the list
# list =[1,2,2,3,4,1,2]
# result=list.count(2)
# print(result)

#remove a specific element from the list
# list =[1,2,3,4,5]
# list.remove(3)
# print(list)

#sort a list in ascending order without using sort method
list=[9,7,8,2,5,1]
# result=sorted(list)
# print(result)
# list.sort()
# print(list)

#find common element b/w two list
# list1=[2,5,7,9,0]
# list2=[7,6,5,4,0]
# list3 = list(set(list1) & set(list2))
# print(list3)

#area of rectangle
# def area_rect(base,height):
#     area=base*height
#     return area
# base =int(input("enter num for base :"))
# height =int(input("enter num for height :"))
# print("area of rectangle is - ",area_rect(base,height),"square feet")

# area of triangle using function
# def area_triangle( area of triangle is -",area_triangle(base,height))

#100 PYTHON PROBLEMS :
#1.input three ages find older one
# a=int(input("enter any num :"))
# b=int(input("enter any num :"))
# c=int(input("enter any num :"))
# if a>b and b>c:
#     print("-a is the older ")
# elif b>c and b>a:
#     print("-b is the older")
# elif a==b or b==c :
#     print("two are equal age")
# else:
#     print("c is the older")

#convert celsius to fahrenheit
# c=float(input("enter the num :"))
# fahrenheit=(c*1.8)+32
# print(fahrenheit,"F")

#swap two nums
#a,b=34,25
# a,b=b,a
# print(a,b)
# tire=a      # by using third variable
# a=b
# b=tire
# print(a,b)

# write a program that will give you sum of three digits
# sum=0
# for i in range(1,4):
#     sum+=i
# print(sum)

#four num digit is reverse and check weather the reverse  is true
# nums=input("Enter any four digit num :")
# result=nums[ : :-1]
# print("the reverse num is :",result)
# final=result[ : :-1]
# if final==nums:
#     print(True)
# else:
#     print(" think it is reversed")

#the num entered by user is odd or even :
# num =int(input("enter any num :"))
# if num%2==0:
#     print("this is even num")
# else:
#     print("this is odd num")

#The given year is a leap year or not
# year=int(input("enter the year :"))
# if (year%400==0) and (year%100==0):
#     print("{} year is a leap year".format(year))
# elif (year%4==0) and (year%100!=0):
#     print("{} year is a leap year".format(year))
# else:
#     print("{} year is a leap year".format(year))
















