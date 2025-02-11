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

#To read total data from the file
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

#Use seek() and tell() method in a single program
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

#Write a program to check whether the given file exists or not. If it is available then print its content?
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

#Program to print the number of lines,words and characters present in the given file
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


















