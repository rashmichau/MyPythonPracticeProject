# This is a sample Python script.
import Basic1

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''f =open("Packaging module",'w')
f.write("it is a python program\n")
f.write("it may helping you for coding\n")
f.write("then you will be a python developer\n ")
print("data written to the file successfully")
f.close()

f=open("Packaging module",'a')
lst=['coding\n','language\n','developer\n','pycharm\n','visual-code\n']
f.writelines(lst)
f.close()'''

# To read total data from the file
'''f=open("Packaging module",'r')
data=f.read()
print(data)
f.close()

f=open("Packaging module",'r')
data=f.readline()
print(data)
data2=f.readline()
print(data2)
data3=f.readline()
print(data3)
f.close()

with open("Packaging module",'r') as f:
    data=f.read(5)
    print(data)
    data2=f.read(3)
    print(data2)
    data3=f.read(15)
    print(data3)
    print("file is close",f.closed)
print("file is closing",f.closed)'''

# The tell() and seek() methods
'''f=open("Packaging module",'r')
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(11))
print(f.tell())'''

# Use seek() and tell() method in a single program
'''data="Python is a object oriented language"
f=open("abc.text",'w')
f.write(data)
with open("abc.text",'r+') as f:
    text=f.read()
    print(text)
    print("The current position of cursor is :",f.tell())
    f.seek(12)
    print("The current position of cursor is :",f.tell())
    f.write("Heigh level ")
    f.seek(0)
    text=f.read()
    print("Data after modification :")
    print(text)'''

# Write a program to check whether the given file exists or not. If it is available then print its content?
'''import os,sys
fname=input("Enter the valid file name :")
if os.path.isfile(fname):
    print("file exists",fname)
    f=open(fname,'r')
else:
    print("File does not exist :",fname)
    sys.exit(0)
print("The content of file is :")
data=f.read()
print(data)'''

# Program to print the number of lines,words and characters present in the given file
'''import os,sys
data="Python has basically many more features for easy code"
fname=input("enter file name :")
if os.path.isfile(fname):
    print("file is exist",fname)
    f=open(fname,'r')
else:
    print("file does not exist",fname)
    sys.exit(0)
lcount=ccount=wcount=0
for line in f:
    lcount=lcount+1
    words=line.split()
    wcount=wcount+len(words)
    ccount=ccount+len(line)
print("number of lines in file",fname,lcount)
print("number of words in file",fname,wcount) 
print("number of words in file",fname,ccount)'''

# Handling csv file
'''import csv
with open("emp.csv",'w',newline="") as f:
    w=csv.writer(f)
    w.writerow(["EMPNUM","EMPNAME","EMPSAL","EMPADDR"])
    n=int(input("enter the employ num :"))
    for i in range(n):
        empnum=input("enter employ number :")
        empname=input(" enter employ name :")
        empsal=input("enter employ salary :")
        empaddr=input("enter employ address :")
        w.writerow([empnum,"\t",empname,"\t",empsal,"\t",empaddr])
print("end of the program")'''

'''def student(a,b=0):
    print(a,b)
student(5 )'''

# Function as an argument
'''def apply_func(func,value):
    return func(value)

def square(x):
    return x**2
result=apply_func(square,5)
print(result)'''

# function as return value
'''def multiplexer(factor):
    def multiplier(x):
        return factor*x
    return multiplier
result= multiplexer(5)
print(result(2 ))'''

'''def f1(n1,n2,n3):
    print(n1)
    print(n2)
    print(n3)
   # print(args)
   # print(kwargs)

f1(8,8,9)'''

# local and global variables
'''a=10
def sum():
    
    a=90
    print(a)
sum()
print(a)'''

# pass list to a function and count even odd numbers
'''def even_odd(lst):
    even = 0
    odd = 0
    for num in lst:
        if num%2==0:
            even+=1
        else:
            odd+=1
    return ("odd num",odd,"even num",even)
lst=[45,58,69,78,23,44,88]
s=even_odd(lst)
print(s)'''

# fibonacci series to the num
'''def fibona(num):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,num):
        c=a+b
        a=b
        b=c
        print(c)
fact(12)'''

'''def fibona(n):
    a=0
    b=1
    c=0
    while(c<=n):
        print(c)
        a=b
        b=c
        c=a+b
fibona(13)'''

''''#Factorial of a number
def fact(num):
    result=1
    for i in range(1,num+1):
        result*=i
    print(result)
fact(0)'''
# fibonacci sequence with the recursive function
'''def fibonacci(n):
    if n<=0:
        return ("result not found")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(9))'''

# Greatest common divisor
'''def gcd(a,b):
    a,b=(b%a,a)
    if a==0:
        return b
    else:
        return gcd(a,b)
print(gcd(42,28))
print(gcd(69,92))
print(gcd(999,567))'''

'''def b (sum_fn):
    a=sum
    return a


def a (c):
    
    return c

def sum():
    b=2+5
    return b'''

'''def decor(func):
    def inner(name):
        func(name)
    return inner

@decor
def f(name):
    print(name)

f("Anjali")'''
# high order functions

from functools import reduce

'''seq=[12,34,54,43,67,23,12]
evens=list(filter(lambda x:x%2==0,seq))
print(evens)
modrate=list(map(lambda x:x*2,evens))
print(modrate)
red=reduce(lambda x,y:x+y,modrate)
print(red)'''

'''s=['1','2','3','4','5','6']
l=("".join(s)).split()
print(l)

st='mjhcdgcnxjjjfkhcx'
lt=st.split(  )
print(lt)

lst=[3,5,6,7,8]
t="".join(str(lst)).split(',')
print(t)'''

'''print("case one ")
try:
    (5/0)
except ZeroDivisionError :
    print('case 2')
else:
    pass
finally:
    print('case 3')


try:
    x=int(input("enter any num :"))
    y=int(input("enter any num :"))
    x/y
except (ZeroDivisionError,ValueError) as msg:
    print("please provide valid num and problem is :",msg)'''

'''def squareIt(x):
    return x**x
assert squareIt(2)==4, "The square of 2 should be 4"
assert squareIt(3)==27, "The square of 3 should be 9"
assert squareIt(4)==256, "The square of 4 should be 16"
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))'''

# Write a Python program to create a Student class and Creates an object to it. method talk() to display student details
"""class Student:
    '''my first code for class'''
    a=90
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        print("constructor executed")
        Student.a=900

    def talk(self):
        print("i am",self.name)
        print("my age is",self.age)
        print("my marks in all subject are",self.marks)
        Student.a=888
print(Student.__doc__)
s1=Student("roohi",36,345)
print(Student.a)
print(s1.a)"""

'''list = [23,4,56,78,43,65,43,12]
list[5]=100
print(list)
import math
print(help (math))'''

# Sum of even num using list of numbers
'''lst=[56,38,76,49,38,99,47,21]
even_nums=[]
odd_nums=[]
for i in lst:
    if i%2==0:
        even_nums.append(i)
    elif i%2!=0:
        odd_nums.append(i)
print(even_nums)
print(odd_nums)'''

# find maximum in tuple without using max inbuilt function
'''tup=(23,56,78,99,567,432)
t=sorted(tup)
print(t[-1])
lst=[]
for i in tup:
    lst.append(i)
    lst.sort()
print(lst[-1])

largest=tup[0]
for i in tup:
    if i>largest:
        largest=i
print(largest)'''

# Remove duplicates from list
'''list=[1,3,6,8,6,5,8,9,4,3,8,8,7]
l1=[]
for i in list:
    if i not in l1:
        l1.append(i)
print(l1)
print(set(l1))'''

# counting frequency of element in list
'''list=[1,2,3,4,5,4,3,2,1,1,1,1,6,6,4,3,3,4,2,]
d={}
for i in list:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''

# Reversing a list without using reverse
'''lst=[45,89,78,56,45,34,23]
l1=[]
for i in range(len(lst)-1,-1,-1):
    l1.append(lst[i])
print(l1)

lst=[67,59,49,30,20,10]
l1=[]
for i in lst:
    l1.insert(0,i)
print(l1)'''

# checking for the prime num
'''def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)'''

# Reverse a String without using slicing or built-in functions.
'''str=input("enter any string :")
ch=''
for i in str:
    ch=i+ch
print(ch)'''

# Remove duplicate elements from a list
'''lst =[2,3,4,5,4,32,45,5,7,7]
l1=[]
for i in lst:
    if i not in l1:
        l1.append(i)
print(l1)'''

# Find the longest substring without repeating characters in a string
'''str =input("enter any str :")
sub=" "
for i in str:
    if i not in sub:
        sub=sub+i
print(sub)'''

# Check if two lists of strings are anagrams of each other.
'''lst1=["a","d","r","e","s"]
lst2=eval(input("make a list"))

if len(lst1)==len(lst2):
    for i in lst1:
        if i  in lst2:
            lst1=lst2
    print("list are anagram")
else:
    print("lists are not anagram of each other")'''

# Find the intersection of two lists.
'''l1=[2,3,4,5,6]
l2=[9,8,7,6]

l3=[]
for i in l1:
    if i in l2:
        l3.append(i)
print(l3)'''

# seprate the even odd nums from a list
'''l2=[]
l3=[]
def lst(l1):
    for i in l1:
        if i%2==0:
            l2.append(i)

        else:
            l3.append(i)
    return (("even nums are",l2),
            ("odd nums are",l3))
l1=[23,4,5,55,67,78,96]
print(lst(l1))'''

# presenting instance variables
'''class marks:
    def __init__(self):
        self.a=67
        self.b=95

    def insub(self):
        self.c=69


c1=marks()
c2=marks()
c1.insub()
c2.insub()
c1.d=93
print(c2.__dict__)
del c2.a
print(c1.__dict__)
print(c1.c)
print(c1.d)'''

# where we can access static variable
'''student:
    a=10
    def __init__(self):
        print(classself.a)
        print(student.a)
    def talk(self):
        print(self.a)
        print(student.a)
    @classmethod
    def marks(cls):
        print(cls.a)
        print(student.a)

    @staticmethod
    def section():
        print(student.a)

s=student()
s.talk()
s.marks()
s.section()
print(student.a)'''

# instance method using of instance variables
'''class student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print("hi ",self.name)
        print("your marks are",self.marks)

    def result(self):
        if self.marks >= 60:
            print("you have passed with first grade")
        elif self.marks >= 50:
            print("you have passed with second division")
        elif self.marks >= 35:
            print("passed with third division")
        else:
            print("you are failed")
n=int(input("enter the number of student :"))
for i in range(n):
    name=input("enter student name")
    marks=int(input("marks gained by student"))
    s=student(name,marks)
    s.display()
    s.result()'''

# operator overloading
'''class book:
    def __init__(self,pages,pages2):
        self.pages=pages
        self.pages2=pages2
    def __add__(self,b1):
         pages= self.pages+b1.pages
         pages2=self.pages2+b1.pages2
         b3 = book(pages,pages2)
         return b3

b=book(100,200)
b1=book(300,400)
b3=b+b1
print(b3.pages)
print(b3.pages2)'''

# str= '''"hfd",'kigff','jhgf','hfddza',"poii"'''
# print(str.isalnum())
# print(str)

# s="".join(str)
# print(s)

l = list(range(2, 12))
# print(l)
# #print(l[1:-1])
# l[3]=300
# print(l)
# l2=[10000,67885,54324,9765]
# l.extend(range(1,23))
'''print(l.sort(reverse=True))
print(l)
y=l[:]
print(y)
y[3]=100
print(y)
print(max(y))
y=l.copy()
y[8]=500
print(y)
print(min(y))
t=l.clear()
print(t)
s=(2,3,4,5,6)
print(max(s))'''

a = (1, 2, 3, 4)
'''b=(4,5,6,7)
t=56
u=89
r=67
o=90
a=t,u,r,o
print(a)

a,b,c,d=a
print(a,b,c,d)

s="raam is a god"
print(s.remove('a'))
l=tuple(filter(lambda x:x%2==0,a))
print(l)'''

# import re
# text="""i am a python developer
# my num 12865559686
# my marks 876 from 1000"""

'''pattern="python"
match=re.search(pattern,text)
print("start index",match.start())
print("end index",match.end())
print(match)

pattern = 
match= re.findall(pattern,text)
print(match)'''

'''p=re.compile("[a-g]")
match=p.findall(text)
print(match)'''

import re

'''count=0
match=re.finditer("ab","abbabbaababab")
for i in match:
    count+=1
    print(i.start(),"...",i.end(),"...",i.group())
print("number of times it occurred",count)
matcher= re.finditer("[]","aS3b1lI4E@")
for match in matcher:
    print(match.start(),"...",match.group())
print(dir())'''

'''n=input("enter any string :")
m=re.match(n,"abcdabcd")
if m!=None:
    print("match found at beginning at the string")
    print(m.start(),"...",m.end())
else:
    print("match does not found at beginning of the string")'''

'''n=input("enter any string :")
m=re.fullmatch(n,"hnf")
if m!=None:
    print("string is full match of pattern",m)
else:
    print("string is not full match of pattern")'''

"""l=re.findall("[a-zA-Z0-9]","avGy3T4K")
print(l)

l2=re.finditer("[a-z]","ahSgrA354fSyud")
for i in l2:
    print(i.start(),"...",i.end(),"...",i.group())

l3=re.subn("[a-z]","@","aP3sE3eW2")
print(l3,l3[0])
print(l3,l3[1])

l4=re.split(" ","i am. the queen.")
print(l4)

s="learning python is beneficial"
l4=re.search("^learning",s)
if l4!=None:
    print("target string starts with searchin string")
else:
    print("target string not starts with searching string")

l5=re.search("beneficial$",s)
if l5!=None:
    print("target string ends with the search string")
else:
    print("target string is not ends with the search string")

'''n=input("Enter a 10 digit number :")
#num=re.fullmatch(r"[7-9]\d{9}",n)
if num != None:
    print("it is a valid number")
else:
    print("it is invalid num,please try again later")"""

# Write a Python Program to check whether the given mail id is valid gmail id or not?
'''mail=input("enter any gmail id :")
mymail=re.fullmatch(r"\w[a-zA-Z0-9]*@gmail[.]com",mail)
if mymail!=None:
    print("your mail id is valid")
else:
    print("invalid,please enter correct mail id")
print(mymail)

import re
s=input("Enter Mobile Number:")
m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
if m!=None:
   print("Valid Mobile Number");
else:
   print("Invalid Mobile Number")'''

import re

match = re.finditer('\d', "Ad3 @r4Wm8")
for i in match:
    print(i.start(), "....", i.group())

pt = "1"
