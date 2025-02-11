# print The Reserve Keyword list
import keyword
import math
# print(keyword.kwlist)

# Integer data type in python
# 1 integral values in Decimal (0,9)
# a = 10
# print(type(a))
# print(id(a))
# print(a)

#2 integral values in binary (1,0)
# a=0B111
# b=0b101
# print(a,b)   bin()=for convert in binary

# 3 integral values in octal (0,7)
# a = 0O24561
# b = 0o674100
# print(a, b)  oct()=for convert in octal

#4 integral values in hexadecimal(0-9 , a-f)
# a = 0x23abf
# b = 0Affdex
# print(a,b)   hex() = for convert in hexadecimal

# float data type in python
# a = 4.6
# print(type(a))
# print(id(a))
# print(a)

#complex deta type
# a = 35+20j
# b = 48+24j
# print(type(a-b))
# print(id(b))
# print(a+b)
# print(a/b)
# print(a*b)

# String deta type
# a = "Rashmi chaudhary"
# b =" Yogesh Chaudhary"
# print(a+b)
# print(b*4)
# print(type(a))
# print(id(a))
# print(a)
# print(a[0])
# print(a[-1])
# output=a[0:len(a)-1]+a[-1].upper()
# print(output)
# print(a[0:7]+a[7].upper()+a[8:16])

# l=[1,"rashmi",(4,6,7),"yogesh",45,9]
# print(type(l))
# print(l)
# print(l[-1])
# print(l[0])
# l.append(10)
# l.remove(1)
# print(l)

# t= (2,"Test",3,4,"rashmi")
# print(type(t))
# print(t)
# print(t[-1])
# print(t[1:4])
# t=( )
# print(type(t)

# s={12,5,6,9,7}
# print(s)
# s=set()
# print(type(s))

# f={10,20,30}
# fs=frozenset( )
# print(f)
# print(type(fs))

# r=range(10)
# print(type(r))
# print(r)
# for i in r:
#     print(i)

# d={100:"yogesh",200:"rashmi",300:"yogirashu"}
# print(type(d))
# print(d)
# d[100]="ushadevi"
# d[200]="kishansingh"
# print(d)

#None deta type
# def f1():
#     print("Hello")
# x=f1()
# print(x)
# print(type(x))
# print(id(x))
#
# userName=input("Enter user name:")
# Pass=input("Enter password:")
# if userName=="Rashmi" and Pass=="Yogesh":
#     print("valid user")
# else:
#     print("invalid user")
#
# a,b = 30,50
# c=16 if a<b else 100
# print(c)

# a=int(input("Enter no:"))
# b=int(input("Enter no:"))
# c=int(input("Enter no:"))
# minima= a if a<b and a<c else b if b<c else c
# print(minima)

#identity operator
# a=["one","two","three"]
# b=["one","two","three"]
# print(a is b)

# def add(x,y):
#     print("performing add operation :")
#     print("the sum is :",x+y)
# def mul(x,y):
#     print("performing mul operation :")
#     print("the multi is:",x*y)
# final=add(3,7)
# final=mul(3,9)

# print(dir(math),end='\n')

# print(math.sqrt(22))
# print(math.pi)
# print(math.e)
# print(math.floor(4.5678))
# print(math.ceil(3.1234))
# print(math.pow(5,3))

#Area of circle
# from math import pi as p
# radius=int(input("Enter no:"))
# area= p*radius**2
# print("The area of circle is",area)
# print(p*pow(radius,2))

# s=input("Enter values:")
# print(s,type(s))
# l=s.split()
# print(l,type(l))
#
# a,b,c=[int(x) for x in input("Enter 3 float numbers with , seperation :").split(',')]
# print("The sum is:",a,b,c)

# x,y,z= int(input("Enter the values"))
# print("The sum is:",x+y+z)

# #find maximum of two no.
# n1=int(input("Enter first no :"))
# n2=int(input("Enter second no :"))
# if n1>n2 :
#     print("n1 is greater than n2",n1)
# elif n1<n2 :
#     print("n2 is gerater than n1",n2)
# else :
#     print("both no are equal")

#find minimum of two no.
# n1 = int(input("Enter first no :"))
# n2 = int(input("Enter second no :"))
# if n1 < n2:
#     print("n1 is smaller than n2 =", n1)
# elif n1 > n2:
#     print("n2 is smaller than n1 =", n2)
# else:
#     print("both no are equal")

#find maximum in three no.
n1 = int(input("Enter first no :"))
n2 = int(input("Enter second no :"))
n3 = int(input("Enter third no :"))
if n1 > n2 and n1>n3 :
    print("n1 is max no =", n1)
elif n2 > n3:
    print("n2 is max no ", n2)
elif n1==n2==n3:
    print("all three no are equal")
else :
    print("n3 is max no =",n3)

































































