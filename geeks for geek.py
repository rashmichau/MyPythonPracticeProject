# import unittest
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
# if __name__ == '__main__':
#     unittest.main()

#right angle triangle pattern
"""n =int(input("enter num of rows :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" *",end=" ")
    print()"""

# simple triangle pattern
"""n=int(input("enter num of rows :"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()"""
#reverse pyramid
"""n =int(input("enter num of rows :"))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()"""

# Random number between float (0,1)
import random
# num= random.random()
# print(num)

#random float num in specified range
# num=random.uniform(1,1000)
# print(num)

# num=random.randint(1,100)
# print(num)

# Factorial series
# x= int(input("enter any num :"))
# fact=1
# if x<0:
#     print("Do not define factorial")
# elif x==0:
#     print("factorial of 0 is always 1")
# elif x>0:
#     for i in range(1,x+1):
#         fact*=i
#     print(fact)
#2
# def fact_(n):
#     if n<=0:
#         return 1
#     return n * fact_(n-1)
# n= int(input("enter any num :"))
# print(fact_(n))

#define fabonacci series :
# num=int(input("Enter the valid :"))
# a=0
# b=1
# c=0
# while(c<=num):
#     print(c)
#     a=b
#     b=c
#     c=a+b

#string palindrome
# str1=input("enter a string :")
# str =str1[ : :-1]
# print(str1)
# if str1==str:
#     print(str,"The palindrome of string ")
# else:
#     print(str,"the string is not palindrome")

# swap case in python
# string="I ma SO TireD 34 35TO"
# print(string.swapcase())

#strip func in python
# str =(input("enter any string :"))
# print(str.rstrip())

#prime numbers
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return 1
#     else:
#         return 0
# n=int(input("enter any num :"))
# P=prime(n)
# if P==1:
#     print("The num is prime num")
# else:
#     print("the num is not prime num")

#num is even or odd
# def check_evodd(n):
#     for i in range(1,n+1):
#         if i%2==0:
#             print(i,"num is even num")
#         else:
#             print(i,"num is odd")
# n=int(input("Enter any num :"))
# check_evodd(n)
#swap two num
# x,y=67,88
# x,y=y,x
# print(x,y)
#num is negative positive or zero
# num=int(input("enter the num :"))
# if num>=0:
#     print(num,"is positive number")
# elif num<0:
#     print(num,"num is negative")
# else:
#     print(num,"please enter valid number")

#sum of n natural num
# num=int(input("enter any num :"))
# sum=0
# if num>0:
#     for i in range(1,num+1):
#         sum+=i
#     print(sum)
# else:
#     print("please enter natural num")

#sum of digit
# num=int(input("Enter the num :"))
# sum=0
# while(num>0):
#     sum=sum+num%10
#     num=num//10
# print(sum)

#square of given num

#square=(lambda x:x**2)
#print(square(int(input("enter num :"))))

#num is palindrome or not
# num=input("enter the string :")
# reverse=num[ : :-1]
# print(reverse)
# if num==reverse:
#     print("num is palindrome")
# else :
#     print("num is not palindrome")

#smaller not
# lst=list(input("enter the list digit :"))
# lst.sort()
# print(lst[0])

# mylst = [5,6,7,89,3,0]
# sum=0
# for i in (mylst):
#     sum=sum+i
# print(sum)

#remove duplicates from list
# lst=[4,7,8,5,9,4]
# newlst=list(set(lst))
# print(newlst)

#reverse the elements
# lst=[56,98,76,37]
# result=lst[ : :-1]
# print(result)
# lst.sort()
# print("in assanding order list element",lst)
# desc=lst[ : :-1]
# print(desc)

#count the num of vowels in string
# def vowels_(str,vowel):
#     final=list(i for i in str if i in vowel)
#     print(final)
# str=(input("Enter the string :"))
# vowel="aeiouAEIOU"
# vowels_(str,vowel)
'''factorial
def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
x=int(input("enter the num :"))
print(fact(x))'''

#palindrome
'''str=input("enter any string :")
finalstr=str[ : :-1]
print(finalstr)
if str==finalstr:
    print("string is palindrome")
else:
    print("str is not palindrome")'''

#prime number
'''num=int(input("enter any num :"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print(num,"is prime number")
else:
    print(num,"is not prime num")'''

#fabonacci
'''num=int(input("enter any num :"))
a=0
b=1
c=0
while(c<=num):
    print(c)
    a=b
    b=c
    c=a+b'''

#reverse of string
'''str=input("enter any string :")
reversedstr=str[ : :-1]
print(reversedstr,"is a revers of input string")'''

#sort of list

'''l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1,len(l1)):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)'''
#second largest number in the list
'''n1=[74,38,29,49,58,99]
n1.sort()
n1.pop(-1)
print(max(n1))'''

#armstrong num
'''num=int(input("enter a three or more then three digit num :"))
sum=0
for i in str(num):
    sum=sum+int(i)**3
print("num cube sum is ",sum)
if (num)==(sum):
    print(num,"is armstrong num")
else:
    print(num,"not a armstrong num")'''

'''n=int(input("enter rows :"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("enter rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()'''

'''n=int(input("enter rows"))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''

'''n=int(input("enter num :"))
sum=0
for i in str(n):
    sum=sum+int(i)
print(sum)'''

'''str="rashmichaudhary"
total=str.count("r")
print(total)'''









