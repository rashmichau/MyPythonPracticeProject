'''class marks:
    def__init__(self,phy,che,maths):
        self.phy=phy
        self.che=che
        self.math=math

    @property
    def percentage():
        return((self.phy+self.che+self.math)/3,"%")
per=marks(50,32,45)'''

'''lst=[1,1,2,3,2,3,4,6,9,9,6]
lis1=[]
for i in lst:
    if not i  in lis1:
        lis1.append(i)
print(lis1)'''

'''lst=[1,1,2,3,2,3,4,6,9,9,6]
lst1={}
for i in lst:
    if i not in lst1:
        lst1[i]=1
    else:
        lst1[i]+=1
print(lst1)'''

# for value in lst1.values():
#     print(value)

# str="this is written by ram "\
#      "also he very brilliant in python code"
# print(str)

# userame="rashmi"
# print(userame)

# def variable():
#     a= "i am python"
#     print(a)
# variable()

# a="i am global"
# def f1():
#     global a
#     a="modified by slab"
#     print(a)
# f1()
# print(a)

# a= [10,20,30,40]
# print(a)
# del(a)
# print(a)

# import keyword
# a=" python keywords as a list are : "
# print(a,keyword.kwlist)

# a=[1,2,3]
# b=a
# c=[1,2,3]
# print(a is b)
# print(b is c)
# print(a is c)

# count=0
# while count<4:
#     count+=1
#     if count==3:
#         break
#
#     print(count)

# for i in range(0,5):
#    pass

# a,b=4,0
# try:
#     k=a/b
#     print(k)
# except ZeroDivisionError:
#     print("we can not divide any value with zero")
#
# finally:
#     print("finally is always printed")

# a="rashmi chaudhary"
# print(a)
# del a
# print(a)
# raise NameError("we are deleting the val of a")

# def fn(a,b):
#     s=a+b
#     return s
# a=int(input("enter any num :"))
# b=int(input("enter any num :"))
# print(fn(a,b))

# def fun(x,y):
#     yield x+y
#     yield x*y
#     yield x*x*y**x
# x=int(input("enter any val:"))
# y=int(input("enter any second val: "))
# for values in fun(x,y):
#     print(values)

# g = lambda x,y,c:x+y*y**x+c
# print(g(9,23,12))

# def fun():
#     var1=10
#     def gun():
#         nonlocal var1
#         var1=var1+1
#         print(id(var1),var1)
#     gun()
#     print(id(var1),var1)
# fun()
#No binding for nonlocal --Error
# global_var="i am global"
# def fun():
#     def gun():
#         nonlocal global_var
#         global_var="i am global"
#         print(global_var)
#     gun()
# fun()

# s="you are a python developer "
# b=" everything is great "
# print(s,b,end ="@",sep='!')
# print(" i am just reading")
# print(f"Hello {s} and {b} you can do it")
# print("it defined with %s" %s)

# lst1=list(input("enter a num list :"))
# lst2=list(input("enter num list :"))
# for i in lst2 :
#     lst1.append(i)
# print(lst1)

# x,y=input().split()
# print(x,y)
# x=list(map(int, input().split()))
# print(x)

# s="bluethink company"
# T=s[1: 9]
# print(T)
# print(len(s))
# print(s.upper())
# print(s.lower())
# print(s.replace('company','model'))

# name1= "Aarun"
# print(name1)
# name2="T"+name1[1:]
# print(name2)

# my_list=list(input())
# my_newstr = " ".join(my_list)
# print(my_newstr)

# str=input("Enter any string :")
# new_str=str[ : :-1]
# print(new_str)

# str="Pythonisobjectorientedlanguage"
# str1=""
# for i in str :
#     str1=i+str1
# print(str1)

'''s = {'dic':2,'sma':3,'sys':4}
print(len(s))
sum=0
for value in s.values():
    sum=sum+value
print(sum)
str=""
for key in s.keys():
    str=key+str
print(str)'''

# str = input("enter a string :")
# count=0
# for i in str:
#     count+=1
# print(count)

# str="Hello"
# for i,char in enumerate(str):
#     print(f"index is{i} : {char}")

# str=['python','is','a','high','level','programming','language']
# a = " ".join(str)
# print(a)

"""str1='''Hello
i am a developer'''
str2 ='''why?
i am doing code ?'''
str3= '''its ok
for being python developer'''
a = str1.splitlines()
b= str2.splitlines()
c=str3.splitlines()

result=[f"{l1} {l2} {l3}"for l1,l2,l3 in zip(a,b,c)]
for line in result:
    print(line)"""

# a = [1,2,6,7,4,3,6]
# c=[]
# for x in a:
#     if x not in c:
#         c.append((x)**2)
# print(c)
#print("Name: \tRashmi \nAge: \t26")

'''class person:
    def __init__(self,name,age,deg):
        self.name=name
        self.age=age
        self.deg=deg

    def __format__(self,f):
        if f =='name':
            return "i am "+self.name
        if f=='age':
            return "my age is"+str(self.age)
        if f=='deg':
            return "my deg is "+self.deg

p = person("Rashmi",26,"Developer")
print(dir(p))
print("{:name}, {:age}".format(p,p))
# # print("{:deg}".format(p))'''

'''def equa_(a,b):
    x = (a*a)+(b*b)+(2*a*b)
    return x

a=int(input("enter value:"))
b=int(input("enter second value :"))

print(f"the expression (a*a)+(b*b)+(2*a*b) value is: {equa_(a,b)}")'''

#makes a sound like a bell
# a='\a'
# print(a)
# print("i am a programmer\
# it is very helpful")

'''def unorganised_data(a,b):
    for i in range(a,b):
        print(i , i**2 , i**3 , i**4)

def organised_data(a,b):
    for i in range(a,b):
        print("{:4d}{:4d}{:4d}{:4d}".format(i,i**2,i**3,i**4))

n1 = int(input("enter any num :"))
n2 = int(input("enter any digit :"))
print("in unorganised manner :")
unorganised_data(n1,n2)
print()
print("in organised manner :")
organised_data(n1,n2)'''

# Input = [100.7689454, 17.232999, 60.98867, 300.83748789]
# output =['{:.2f}'.format(i) for i in Input]
# print(output)

# English=94
# Maths=95
# Science=98
# print(f"the total parentage is {(English+Maths+Science)/3} from marks 300 ")

# lst =[]
# n = int(input("enter a num :"))
# for i in range (n):
#     element = input(f"Enter element {i+1} :")
#     lst.append(element)
# print("list:",lst)

# n=int(input("Enter the value :"))
# for list in range(4):
#     l1=[input(f"Enter element{i+1}:") for i in range(n)]
#     print(l1)

'''li =[1,2,3]
si =[0,2]
li.append(4)
li.extend([4,8,9])
li.insert(5,6)
t=li+si
print(t)
print(li)
n=[li[i]for i in si]
print(n)
m=[item for item in li if item>-1]
print(m)

a=[3,5,8,6]
for index,value in enumerate(a):
    print(index,value)
s =[(i,a[i]) for i in range(len(a))]
print(s)'''

'''l=[5,10,15,20,25]
l1=[x*2 if x%2==0 else x for x in l]
print(l1)

for i,x in enumerate(l):
    if x%2!=0:
        l[i]+=5
print(l)

a=[10,20,30,40,50]
for i in range(len(a)):
    if a[i]==30 :
        a[i]=99
print(a)'''

'''a=['sun','rise','in','East']
s=a.insert(0,'The')
print(a)
m="".join(a)
print(m)'''

'''a =[20,35,46,89,67,50]
key = 50

if key in a:
    print(key,"is exist in list a")
else:
    print(key,"is not present in list a")'''

'''class student:

    def __init__(self,maths,science):
        self.maths=maths
        self.science=science
    def conf(self):
        print("the ,arks in  subject are :",self.maths,self.science)

s1=student(78,42,)
s2=student(74,56)
s1.conf()
student.conf(s2)
print(id(s1))
print(id(s2))'''

'''class computer:

     def __init__(self):
         self.name= 'rashmi'
         self.age=25

     def update(self):
         self.age=30

     #def compare(self,other):


c1=computer()
c2=computer()
c1.name='yogesh'
c1.age=32
c2.update()
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age )'''

'''class student:

    def __init__(self):
        self.name='rashmi'
        self.marks=298

    def compare(self,other):
        if self.marks==other.marks:
            return True
        else:
            return False


s1=student()
s2=student()
s2.marks =300
print(s1.marks)
print(s2.marks)
if (s1.compare(s2)):
    print("the same marks")
else:
    print("the different marks")'''



# def dict_man():
#     dict_data = {"name":"ashutosh","age":25,"add":"noida"}
#     for key,value in dict_data.items():
#         print(key,":",value)
#
# dict_man()

'''lst1 =[2,4,6,8]
lst2=[9,11,7,8]
l3=lst1+lst2
print(l3)

lst1.extend(lst2)
print(lst1)'''

#a =[1,2,3,4,5]
# t =bytes(a)
# print(type(t))
# for i in a:print(i)
#b=a*2
#print(b)

# r=range(10,20)
# for i in r: print(i,end=",")
# i[4]=23
# print(i)

# d ={100:"ravi",101:"raam",102:"raghav",103:"rajan"}
# d['a']=111
# d['b']=122
# d[100]="krishna"
# print(d)

# s=10+5j
# t=s.imag
# print(t)

# s=bool ("")
# print(s)

# a=int(input("enter the first val :"))
# b=int(input("enter the second val :"))
# min =a if a<b else b
# print("The min value is :",min)

# a,b=[int(x) for x in (input("enter any two numbers :").split())]
# print("The product is :",a*b )

# a,b,c=[float(x) for x in input("Enter any three float values :").split(',')]
# print(a,b,c)
# print("the sum of all three num is :",a+b+c)

# from sys import argv
# print(len(argv))
# print(argv)
# for i in argv:
#     print(i)

#from sys import argv
# sum=0
# args=argv[1:]
# for x in args   :
#    n=int(x)
#    sum=sum+n
# print("The Sum:",sum)
#print(argv[1])

# a =10
# b=20
# c=30
# print("a value is %s" %a)
# print("b value is %d and c value is %d"%(b,c))

#conditional statements

#Biggest of given two nums
'''num1 =int(input("Enter the num1 :"))
num2 =int(input("enter the num2 :"))
num3 =int(input("Enter the num3 :"))
if num1>num2 and num1>num3:
    print(num1,"is the biggest")
elif num2>num3:
    print(num2,"is the biggest")
else:
    print(num3,"is biggest")'''

# Write a program to find smallest of given 2 numbers?
'''a= int(input("enter num :"))
b= int(input("enter the num :"))
c= int(input("enter the num :"))
if (a<b) and (a<c):
    print(a,"is smaller")
elif (b<c):
    print(b,"is smaller")
elif (a==b==c):
    print("all nums are equal")
else:
    print(c,"is smaller")'''

#Write a program to check whether the given number is even or odd?
'''def even_odd(num):
    if num%2==0:
        print(num," is even number")
    else :
        print(num,"is odd number")

num =int(input("Enter any number:"))
even_odd(num)'''

#Write a program to check whether the given number is in between 1 and 100?
'''def num_range(num):
        if num  in range(1,101) :
            return (num,"is in range 1 to 100")
        else:
            return (num,"is not in range  1 to 100")

num = int(input("Enter num in any range :"))
print(num_range(num))'''

#Write a program to take a single digit number from the keyboard and print is value in English word?
'''num = int(input("Please enter single digit number :"))
if num==0:
    print("Zero")
if num==1:
    print("one")
if num==2:
    print("Two")
if num==3:
    print("Three")
if num==4:
    print("Four")
if num==5:
    print("five")
if num==6:
    print("six")
if num==7:
    print("seven")
if num==8:
    print("eight")
if num==9:
    print("Nine")'''

#iterative statements
'''s = input("enter any string :")
i=0
for x in s:
    print("string index",i,"have word :",x)
    i+=1

# To display odd numbers from 0 to 20
for i in range(21):
    if i%2!=0:
        print(i,"num is odd")'''

#To display numbers from 10 to 1 in descending order
'''for i in range(10,0,-1):
    print(i,end=",")'''
#To print sum of numbers present inside list
'''lst = (input("enter num with space :").split())
print(lst)
sum=0
for i in lst:
    sum =sum+int(i)
print(sum)'''

# To print numbers from 1 to 10 by using while loop
'''i=1
while i<=10:
    print(i)
    i=i+1'''

#To display the sum of first n number
'''n=int(input("enter any num :"))
i=1
sum =0
while i <= n:
    sum = sum+i
    i = i+1
print(sum)'''

# Nested loops
#right angle triangle
'''n=int(input("enter num of rows :"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("Enter any num :"))
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n=int(input("enter num of rows :"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()'''

#Transfer statement
'''for i in range(0,10):
    if i==7:
        print("processing is failed")
        break
    print(i)

cart =(input("enter num with space :").split())
print(cart)
for i in cart:
    if int(i)>500:
        print("More rules are apply for the shipment :")
        break
    print(i)'''

'''cart = [45,67,89,500,700,78,34,200]
for item in cart:
    if item>=500:
        print("we can not process with this item :",item)
        continue
    print(item)
else:
    print("stop the code")'''

#Write a program to accept some string from the keyboard and display its characters by
#index wise(both positive and negative index)
'''s = input("Enter any string :")
i=0
for x in s:
    print("the positive index  {} and negative index {} of string element  {}".format(i,i-len(s),x))
    i=i+1'''

'''s=input("enter any string :")
print("forward dirn ")
for i in s[::]:
    print(i,end="")

print("backward direction")
for i in s[::-1]:
    print(i,end="")'''

'''s="learning Python is very easy"
subs=input("Enter any substring:")
print(s.find('Python'))
print(s.find('r'))
print(s.find('very'))
print(s.find('a'))
try:
    (s.index(subs))
except ValueError:
    print("substring not found in string")
else:
    print("Substring is found in string")'''

# Program to display all positions of substring in a given main string
'''str=input("enter any string :")
subs=input("enter any substr :")
n=len(str)
pos=-1
while True:
    pos=str.find(subs,pos+1,n)

    if pos==-1:
        break
    print("the substrat index",pos)


else:
    print("please mention some right code")'''

'''s="python is programing language"
l=s.split()
print(l)
st="02 34 4567"
lt=st.split()
print(lt)
p=":".join(lt)
print(p)'''

#reverse string
'''s="python is a very easy to learn language"
str=''
for ch in s:
    str=ch+str
print(str,end="")'''

'''s="Python is object oriented language"
str=[]
i=len(s)-1
while i>=0:
    str.append(s[i])
    i=i-1
output=''.join(str)
print(output)'''

# list int element convert into str
'''lst=[17,20,19,8,7]
strl=[]
for i in lst:
    strl.append(str(i))
print(strl)'''

'''l='ABCABCABBCEYD'
s={}
for i in l:
    if i not in s:
        s[i]=1
    else:
        s[i]+=1
for key,value in s.items():
    print("{} = {}".format(key,value),end=",")'''

'''s='a4k3b2'
for i in s:
    if i.isalpha():
        print(i,end="")
for j in s:
    if j.isdigit():
        j=int(j)
        print((j),end="")'''

'''str="ASFUEWSAADDVCCCHUUY"
l=[]
for i in str:
    if i not in l:
        l.append(i)
    output=''.join(l)
print(output)'''

'''class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
print("{p.name}'s age is {p.age}".format(p=person("rashmi",36)))
p=person("Rashmi",36)
p.age=25
print(p.name)
print(p.age)'''

'''import datetime
time=datetime.datetime.now()
print("It's now:{:%d/%m/%Y  %H:%M:%S}".format(time))

comp=10+20j
print("The real part is {0.real} and img part is{0.imag}".format(comp))'''

'''l=list(range(0,20,2))
x=len(l)
for i in range(x):
    print("positive index",i,"and negative index",i-x,"of element",l[i])


s="rashmi is a very good girl"
print(list(s))

t=s.split()
print(t)
print(s.count('a'))
t.insert(3,6)
print(t)'''

'''order=['chicken','mutton','mushroom']
isto=["triangulable"]
order.extend(isto)
order.remove('chicken')
print((order))
order.reverse()
order.sort()
order.sort(reverse=False)
print(order)'''

'''s=[77,98,42,33,45]
t=s+[4]
print(t)
print(s*3)

x=["Dog","Cat","Rat"]
y=["Rat","Cat","Dog"]
print(x<y)
x.clear()
print(x)'''

# List comprehension
'''s=[x*x for x in range(1,11)]
print(s)
r=[2**x for x in range(2,8)]
print(r)
m=[x for x in range(50) if x%2==0]
print(m)
words=['cat','rat','animals','humans','squirrel']
a=[w[0] for w in words]
print(a)'''

'''words="The quick brown fox jump over the black dog".split()
print(words)
s=[(w.upper(),len(w)) for w in words]
print(s)'''

#Write a program to display unique vowels present in the given word?
'''def vowel(str):

    for v in str:
        print("yes found")

vowel="aeiouAEIOU"
str=input("enter any string :")
found=[]
for latter in str:
    if latter in vowel:
        print(latter,end="")
        found.append(latter)
print(found)
print("the num of vowel present instr is",len(found))'''

'''t = eval(input("Enter any nums :"))
sum=0
l=len(t)
for i in t:
    sum=sum+i
print("the sum of nums in tuple is : ",sum)
print("the average of tuple is",(sum)/3)'''

# str="python is a language"
# t=str.split()
# print(t)

#Write  a program to enter name and percentage  marks in a dictionary and display information on the screen
'''dict={}
n=int(input("enter number of students :"))
i=0
while(i<=n):
    name=input("enter student name:")
    marks=input("enter marks of student :")
    dict[name]=marks
    i=i+1
print("name of student",'\t',"marks of student")
for x in dict:
    print("\t",x,"\t",dict[x])'''

#Write a program to take dictionary from the keyboard and print the sum of values?
'''dic={'n':100,'w':200,'r':300,'e':400}
sum=0
for value in dic.values():
    sum+=value
print(sum)
#type 2
s=sum(dic.values())
print(s)'''

'''word=input("enter any string :")
d={}
for i in word:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
for k,v in d.items():
    print(k,"occured",v,"times")'''

# def f1():
#     print("hello")
# print(type(f1()))

#Write a function to check whether the given number is even or odd?
'''def f1(n):
    if n%2==0:
        print(n,"Even num")
    else:
        print(n,"is odd one")
n=int(input("Enter any value :"))
f1(n)'''

#Write a function to find factorial of given number?
'''def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n= int(input("Enter any value :"))
print(fact(n))'''

#Returning multiple values from a function:
'''def multiple_val(a,b):
    mult=a*b
    div=a/b
    sum=a+b
    sub=a-b
    return mult,div,sum,sub
a=int(input("enter any num :"))
b=int(input("enter any val"))
print(multiple_val(a,b))'''

#We can mix variable length arguments with positional arguments.
'''def variable_(n1,*n):
    sum=0
    print(n1)
    for i in n:
        sum=sum+i
    return sum
print(variable_(10,20,30,40,50))
print(variable_(90,82))'''

#call this function by passing any number of keyword arguments
'''def  key_word(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)

key_word(maths=34,scie=35,hindi=36,eng=40)
key_word(kuc="name",age=45,ter="nominate")'''
'''a=20
def f1():
    a=10
    print(a)
f1()
def f2():
    print(a)
f2()'''

#Write a program to create a lambda function to find square of given numbers ?
'''square=lambda x:x**2
print("square of 5 is",square(5))'''

#Lambda function to find sum of 2 given numbers
'''sum=lambda a,b:(a+b)
print("the given expression is",sum(6,80))'''

#Lambda Function to find biggest of given values.
'''compare=lambda a,b:a if a>b else b
print("The biggest from a&b is",compare(25,39))'''

#Program to filter only even numbers from the list by using filter() function?
'''def is_even(n):
    if n%2==0:
        return True
    else:
        return False
l=[10,5,20,25,30,49]
l1=list(filter(is_even,l))
print(l1)'''

'''l=[34,67,80,93,55,67,87,90]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)'''

#For every element present in the list perform double and generate new list of doubles.
'''l=[1,2,3,4,5,6]
def square(n):
    return n*2
l1=list(map(square,l))
print(l1)'''

'''l=[10,20,30,40,50]
doublet=list(map(lambda x:x*2,l))
print(doublet)'''

from functools import *
'''l=[20,30,40,50,60]
sum =reduce(lambda a,b:a+b,l)
print(sum)

sum=reduce(lambda a,b:a*b,range(1,101))
print(sum)'''
#this without touching wish() function by using decorator.

'''def decor(func):
    def inner(name):
        if name=="reema":
            print("Hello reema today morning is very good")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("Hello",name,"Good morning")
wish("raam")
wish("suney")
wish("reema")'''

#Program for decorator Chaining:
'''def decor(func):
    def inner(name):
        print("first Decor(decor) func executed")
        func(name)
    return inner
def decor1(func):
    def inner(name):
        print("second Decor(decor1) func executed")
        func(name)
    return inner
@decor1
@decor
def wish(name):
    print("Hello i am",name,"in Python field")
wish("rashu")
wish("tarun")
wish("arifa")'''

#Generators
'''def my_gen() :
    yield 'A'
    yield 'B'
    yield 'C'
g= my_gen()
print(type(my_gen()))
print(next(g))
print(next(g))
print(next(g))
print(next(g))'''

'''def countdown(num):
    print("Start countdown")
    while(num>0):
        yield num
        num=num-1
values=countdown(5)
for i in values:
    print(i)'''

#To generate first n numbers:
'''def natural_num(num):
    print("starting of natural num")
    i=1
    while i<=num:
        yield i
        i=i+1

series=natural_num(10)
l1=list(series)
print(l1)

for i in series:
   print(i)'''

# To generate Fibonacci Numbers...
'''def fibona(num):
    print("fibonacci series is")
    a,b,c=0,1,0
    while(c<=num):
        yield(c)
        a,b=b,c
        c=a+b
series=fibona(100)
for i in series:
    print(i)'''

'''a=10
b=20
def f1():
    print("Hello")
print(dir())
f1()'''




















