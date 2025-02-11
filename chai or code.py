#conditional statement questions
# age = int(input("Enter the age :"))
# if (age <=13) :
#     print("He/She is child ")
# elif (13<age<=19) :
#     print("He/She is teenager")
# elif (20<=age<60) :
#     print("He/She is adult")
# elif (age>=60) :
#     print("He/She is senior")


# age = int(input("Enter the age :"))
# price= int(input("Enter the price in :$"))
# if (age >=18) and (price==12):
#     print("adults can watch movie in theater")
# elif (age<18) and (price==8):
#     print("child can watch movie")
# elif (age>=18 and price>=10) or (age<18 and price>=6):
#     print(f" Yes on wednesday age {age} watch movie on discount")
# else:
#     print(" not allowed in theater with this price")

#Factorial series
# fact = 1
# num=int(input("Enter the digit :"))
# if num<0:
#     print("not defined for negative num")
# if num==0:
#     print("it is return 1")
# if num>0:
#    for i in range(1,(num+1)):
#       fact*=i
#    print(fact)

#fabonacci series
# num = int(input("Enter the series num :"))
# a = 0
# b = 1
# c = 0
# while (c<=num) :
#     print(c)
#     a=b
#     b=c
#     c=a+b

#String is a palindrome
# sub = input("Enter any string :")
# n = sub[ : :-1]
# if n==sub :
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

#Reverse a string
# st = input("enter string :")
# n = st[ : :-1]
# print("Reverse of given string:",n)

# Find Prime no
# num = int(input("Enter any num :"))
# count=0
# i=1
# while(i<=num):
#     if (num%i==0):
#         count+=1
#     i+=1
# if (count==2):
#     print("num is prime no",num)
# else:
#     print("num is not prime no")

#Using function for prime no
# def prime(n):
#     count=0
#     for i in range(1,(n+1)):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return 1
#     else:
#         return 0
# n = int(input("Enter any digit :"))
# P = prime(n)
# if (P==1):
#     print("num is prime",n)
# else:
#     print("num is not prime")

#Chech weather a num is even or odd
# num = int(input("Enter any num :"))
# if (num%2==0) :
#     print("it is a even no :",num)
# else:
#     print("it is an odd one")

#swap two numbers
# x = int(input("Enter val of x :"))
# y = int(input("Enter val of y :"))
# x,y = y,x
# print("the value of x = ",x)
# print("the value of y = ",y)

#num is negative,positive or zero
# num = eval(input("Enter any no :"))
# if num==0:
#     print("num is zero and value is ",num)
# elif num>0:
#     print("num is positive and value is ",num)
# else:
#     print("num is negative and value is",num)

#Sum of first n natural numbers
# n = int(input("Enter the num :"))
# if n>0:
#     for i in range(1,(n+1)):
#         i +=n
#     print("sum of first n natural num is = ",i)
# else:
#     print("num is not natural no")

#The largest of three numbers
# n1 = int(input("Enter The num1 :"))
# n2 = int(input("Enter The num2 :"))
# n3 = int(input("Enter The num3 :"))
# if (n1>n2) and (n1>n3):
#     print("n1 is the largest = ",n1)
# elif n2>n1 and n2>n3:
#     print("n2 is largest = ",n2)
# elif n1==n2 or n2==n3 or n1==n3:
#     print("Two no are equaland other one is the smaller")
# elif n1==n2==n3:
#     print("all no are equal")
# else:
#     print("n3 is largest = ",n3)

#1 to 100 divisible by 5
# n = int(input("Enter any no:"))
# for i in range(1,n+1):
#     if i%5==0:
#         print(i,"Yogirashu")
# else:
#     print("that's all my love Ogesh ")

#Sum of digits for a n
# def the_sum(num):
#     sum=0
#     while(num>0):
#         sum=sum+num%10
#         num=num//10
#     return sum
# t=the_sum(45678)
# print(t)
#
# num=(input("enter the digit :"))
# sum = 0
# for i in str(num):
#     sum = sum+int(i)
# print(sum)

#reverse num
# num = str(input("Enter any digit :"))
# s = num[ : :-1]
# print(s)

#Square of given num
# n = int(input("Enter thr num :"))
# s = (n**2)
# print(f'square of {n}  is {s}')

#check num is palindrome or not
# str = str(input("enter the palindrome :"))
# st = str[ : :-1]
# if str==st:
#     print("it is palindrome ")
# else:
#     print("it is not palindrome")

#Smallest no in a list
# a = list(input( "enter list digits:"))
# print(a)
# a.sort()
# print("smaller no is",a[0] )

#remove duplicate from list
# lst = [1,1,2,2,3,3,6,7,9,4]
# print(list(set(lst)))

#sum of element in list
# mylist= [1,2,3,4,5]
# total = sum(mylist)
# print(total)

#count specific  item in list
# digit = (input("enter the count digit :"))
# mylist = [4,'b',6,'a',9,7,6,'rashuyogi',6,'rashuyogi',4,'b',9,'a',5,7]
# total = mylist.count(digit)
# print(total)

# check list is empty
# mylist=list(input('enter elements :'))
# print(mylist)
# if mylist!=[]:
#     print("list is not empty")
# else:
#     print("list is Empty")

#reverse the elements of list
# mylist = ["rashuyogi","Yogesh","rashu",1,4,3]
# result = mylist[ : :-1]
# print(result)

#sort list in ascending order
# mylist = [3,9,88,65,45,78]
# mylist.sort()
# print(mylist)

#add an element end of the list
# mylist = list(input("enter ele of list :"))
# print(mylist)
# ele = list(input("Element :"))

# mylist.append(ele)
# print(mylist)

#find max and min in the list
# mylist = list(input("enter the elements of list: "))
# print(max(mylist))
# print(min(mylist))

#square of num from 1 to 10
# mylist = list(i**2 for i in range(1,11) )
# print(mylist)

#count the num of vowels in string
# def my_vow(string,vowels):
#     final = [i for i in string if i in vowels]
#     print(len(final))
#     print(final)
# string = input("enter any string: ")
# vowels = "AaEeIiOoUu"
# my_vow(string,vowels)

#reverse the sentence
# sent = input("enter any sentence :")
# reverse = sent[ : :-1]
# print(reverse)

#check string is a palindrome
#string = input("enter any string :")
# reverse = string[ : :-1]
# if string==reverse:
#     print("yes string is palindrome")
# else:
#     print("string is not palindrome")

#replace all space in -
# string = input("enter any string with spaces :")
# x = string.replace(" ","-")
# print(x)

#count the num of vowels in string without fn
# string = input("enter any string :")
# vowel = "AaEeIiOoUu"
# final = [i for i in string if i in vowel]
# print(len(final))
# print(final)

#check string contain only digits
# string =(input("enter any string :"))
# if string.isdigit():
#     print("string contains only digits")
# else:
#     print("string contain all the elements")

#find length of string
# mystring = input("Enter an string :")
# print(len(mystring))

#concatenate two string
# str1 = input("enter any str1 :")
# str2 = input("Enter any str2 :")
# total = str1 + str2
# print(total)

#remove all spaces from string
# string = input("Enter any string :")
# test = string.replace(" ","")
# print(test)

#count num of characters in string
# string = str(input("enter any string elements :"))
# x = len([i for i in string if i.isalpha()])
# print(x)

#multiplication table of any num
# num = int(input("enter any num :"))
# for i in range(1,11):
#     print(num,"x",i,"=",(num*i))

#print all even num b/w 1 and 100
# n = int(input("enter any num :"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,end=',')

#first n even num
# n = int(input("enter any digit :"))
# for i in range(n+1):
#     if i%2==0:
#         print(i)

#check num is prime
# n= int(input("enter any num :"))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("num is prime")
# else:
#     print("num is not prime")

#sum of all odd n num
# n = int(input("enter any num :"))
# result=0
# for i in range(n+1):
#     if i%2!=0 :
#         result=result+i
# print(result)

#factorial of a num
# n = int(input("enter any digit:"))
# result=1
# for i in range(1,n+1):
#     result=result*i
# print(result)

#num b/w 1and100 divisible by both 3 and 7
# n = int(input("enter any num :"))
# for i in range(1,n+1):
#     if i%3==0 and i%7==0:
#         print(i)

#sum of square of first n natural num
# n = int(input("enter the num :"))
# sum=0
# for i in range(1,n+1):
#     i = i**2
#     sum = sum+i
# print(sum)

#all prime num b/w 1and50
# n = int(input("enter num :"))
# count=0
# for num in range(1,n+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)















