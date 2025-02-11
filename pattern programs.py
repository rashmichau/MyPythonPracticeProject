# pattern of right angle triangle
# num = int(input("enter num of rows :"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#pattern for odd num in right angle triangle
# num = int(input("enter the num of rows :"))
# k = 1
# for i in range(1,num+1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     k +=2
#     print()

#pattern for pyramid
# num = int(input("Enter the num of rows :"))
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print( )

# gcd of two nums:
# def gcd_hcf(x,y):
#     if x>y :
#         smaller= y
#     else:
#         smaller= x
#     for i in range(1,smaller+1):
#         if(x%i==0 and y%i==0):
#             hcf=i
#     return hcf
# num1= int(input("enter any num1 :"))
# num2= int(input("enter any num2 :"))
# print("the Gcd of two num is",gcd_hcf(num1,num2))

# def lc_m(x,y):
#     if x>y :
#         greater = x
#     else:
#         greater = y
#     while (True):
#         if (greater%y==0 and greater%x==0):
#             lcm = greater
#             break
#         greater +=1
#     return lcm
# num1=int(input("enter num1 :"))
# num2=int(input("enter num2 :"))
# print("lcm of two num is : ",lc_m(num1,num2))

#sum of digits of num
# num = (input("enter any num :"))
# sum=0
# for i in str(num):
#     sum =sum+int(i)
# print(sum)

#square of num without using multiplication
# num = int(input("enter any digit :"))
# result = pow(num,2)
# print(result)

#convert a decimal number to binary
# num = float(input("enter any digit :"))
# num2 =bin(int(num))
# print(num2)

# num is perfect square or not
# num = int(input("enter any num :"))
# prsqrt =(num**0.5)
# if (prsqrt**2 == num):
#     print("number is a perfect square")
# else:
#     print("num is not perfect square")

#greater in three nums:
# a =int(input("enter any num:"))
# b =int(input("enter any num:"))
# c =int(input("enter any num:"))
# if a>b and a>b :
#     print("a is greater num")
# elif b>c :
#     print("b is greater num")
# else:
#     print("c is greater num")

#all factors of given num:
# def factor_giv(x):
#     print("all factors of",x,"is :")
#     for i in range(1,x+1):
#         if (x%i==0):
#             print(i)
# num = int(input("enter any digit for factor :"))
# factor_giv(num)

#multiplication of two num without using * operator:
# def mul_tiple(x,y):
#     pro = 0
#     for _ in range(x):
#         pro = pro+y
#     print(pro)
# num1=int(input("enter num1 :"))
# num2=int(input("enter num2 :"))
# mul_tiple(num1,num2)

#power of a num using loop :
# num = int(input("enter any num :"))
# power = int(input("enter any num :"))
# calculation = num**power
# while True:
#     print(calculation)
#     break
# else :
#     print("bye bye")

# print num from 1 to 10 using for loop
# print("num 1 to 10 is :")
# for i in range(1,11):
#     print(i)

#print the element of list one by one
# my_list = [10,20,30,40,50]
# for i in my_list:
#     print(i)

#sum of all num from 1 to 50
# sum =0
# for i in range(1,51):
#     sum =sum+i
# print(sum)

#all even num from 1 to 20
# for i in range(1,20):
#     if (i%2==0):
#         print(i)

#print each character of a string
# my_string = "Python"
# for i in my_string :
#     print(i)

# iterate through a list of num and print
# weather each num is odd or even
# numbers = [1,2,3,4,5,6,7,8,9]
# for i in numbers:
#     if (i%2==0):
#         print("number is even =",i)
#     else:
#         print("num is odd =",i)

#factorial of given num using for loop
# factor=1
# num = int(input("enter any num :"))
# if num<0:
#     print("factorial is not work for negative nums")
# if num==0:
#     print("factorial for zero is always 1")
# if num>0:
#     for i in range(1,num+1):
#         factor*=(i)
#     print(factor)

# largest num in list using for loop
# lst = []
# num = int(input("enter nums of element in list :"))
# for i in range(0,num):
#     ele = int(input())
#     lst.append(ele)
# print(lst)
# largest =max(lst)
# print(largest)

#reverse a string using for loop
# my_string="python"
# rev = ""
# for i in my_string:
#     rev=i+rev
# print(rev)

#print multiplication table of a given number:
# num = int(input("enter the num :"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# count the num of vowels in a string
# string = input("enter string :")
# vowels = "aeiouAEIOU"
# count = sum(string.count(vowel) for vowel in vowels)
# print(count)

#sorted in ascending order using for loop
# lst = [22,78,65,45,44]
# for i in lst:
#     lst.sort()
# print(lst)

#creat new list that contain the square of each num from original list
lst =[]
# num = int(input("enter element for list :"))
# for i in range(0,num):
#     ele =int(input())
#     lst.append(ele**2)
# print(lst)

#fibonacci series up to n terms using for loop
# n =int(input("enter num :"))
# a=0
# b=1
# c=0
# for i in range(0,n+1):
#     if c<=n:
#         print(c)
#     a=b
#     b=c
#     c=a+b

#sum of digits of given num using for loop
# num = int(input("enter any num with digits :"))
# sum=0
# for i in str(num):
#     sum=sum+int(i)
# print(sum)

#check a string is palindrome or not
# mystring = input("Enter any string :")
# result = mystring[ : :-1]
# if mystring==result:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")
# print(result)

#function to check if two string are anagrams
# def check(x,y):
#     if (sorted(x)==sorted(y)):
#         print("strings are anagrams")
#     else:
#         print("strings are not anagrams")
# x = input("Enter string 1 :")
# y = input("Enter string 2 : ")
# check(x,y)

# check substring
# a = input("Enter any string :")
# b = input("Enter any string :")
# if a in b :
#     print("a is  substring of b")
# else:
#     print("a is not substring of b")


#count frequency of each character in string
# my_string = input("Enter the string :")
# freq = { }
# for char in my_string :
#     freq.setdefault(char,0)
#     freq[char]+=1
# print("the freq count of each char :"+str(freq))

#fibonacci series of n nums
# n = int(input("enter the num :"))
# a=0
# b=1
# c=0
# while(c<=n):
#     print(c)
#     a=b
#     b=c
#     c=a+b

#num is prime or not
# num = int(input("enter any digit :"))
# count=0
# i=1
# while (i<=num):
#     if(num%i==0):
#         count+=1
#     i+=1
# if count==2:
#     print("num is prime ")
# else:
#     print("num is not prime")













