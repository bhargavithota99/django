# @modules
# def add(x,y):
#         print(x+y)
# def sub(x,y):
#         print(x-y)
# def mul(x,y):
#     print(x*y)
# def div(x,y):
#     print(x/y)
##@File Handling
# f=open("Bhargavi.txt",'w')
# f.write("Hai,Iam from Nellore")
# f.close()
# f=open("Bhargavi.txt","r")
# print(f.read(2))
# f.close()
# f=open("Bhargavi.txt","r")
# print(f.readline())
# f.close()
# f=open("Bhargavi.txt","r")
# print(f.readlines())
#print(f.readline())
#print(f.readline())
#f.close()
# f=open("Bhargavi.txt","r")
# for x in f:
#     print(x)
# f=open("Bhargavi.txt","a")
# f.write("Iam the best")
# f.close()
# f=open("Bhargavi.txt","r")
# print(f.read())
# f=open("hello.txt","w")
# f.write("hello")
# f.close()
# f=open("D:/Bhargavi.txt","w")
# f.write("hai,hello")
# f.close()
# f=open("D:/Bhargavi.txt","r")
# print(f.read())
# f.close()
# import os
# os.rename("D:/Bhargavi.txt","D:/Bhargavi1.txt")
# import os
# os.mkdir("D:/Rakesh")
# import os
# os.chdir("D:/Rakesh")
# print(os.getcwd())
# import os
# os.rename("D:/Rakesh","D:/Janasena")
# import os
# os.mkdir("D:/India")
# os.rmdir("D:/India")
# f1=open("hello.JPG","rb")
# f2=open("bhargavi.jpg","wb")
# bytes=f1.read()
# f2.write(bytes)
# print("image name:","bhargavi.jpg")
# import os
# os.remove("hello.txt")
# @context processors:
# with open("Bhargavi.txt","r") as f:
#     for line in f:
#         print(line)
# with open("Bhargavi.txt","a",encoding='utf8') as f:
#     f.write("\n数据分析")
# with open("test.csv","r") as f:
#     print(f.read())
##@Exception Handling
# a=10
# b=0
# try:
#     print(a/b)
# except ZeroDivisionError as e:
#        print(e)
# else:
#     print("else")
# finally:
#     print("final block")
# a=10
# b=0
# try:
#     print(a/b)
# except Exception as e:
#        print(e)
# else:
#     print("else")
# finally:
#     print("final block")
# @user defined Exceptions:
# class Validate(Exception):
#     pass
# age=int(input("Enter your age:"))
# try:
#     if  age<19:
#         raise Validate
# except Validate as e:
#     print("He is not eligible")
# else:
#     print("He is eligible")
# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")
# @polymorphism
# @Method overriding
# from math import pi
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def area(self):
#         pass
#
#     def fact(self):
#         return "I am a two-dimensional shape."
#
#     def __str__(self):
#         return self.name
# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length
#
#     def area(self):
#         return self.length**2
#
#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
#
#     def area(self):
#         return pi*self.radius**2
# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())
# @@Multithreading
# from threading import*
# print("The current thread is:",threading.current_thread().getName())
# def display():
#     for i in range(10):
#         print("child Thread")
# t=Thread(target=display)
# t.start()
# for i in range(10):
#     print("main Thread")
# method-2
# from threading import*
# class MyThread(Thread):
#     def run(self):
#         for i in range(10):
#             print("child Thread")
# t=MyThread()
# t.start()
# for i in range(10):
#     print("main Thread")
# Method-3:
# from threading import*
# class Test:
#     def m1(self):
#         for i in range(10):
#             print("child Thread-1")
# obj=Test()
# t=Thread(target=obj.m1)
# t.start()
# for i in range(10):
#     print("main Thread-1")

# Function
# def add(x,y):
#     c=x+y
#     d=x-y
#     return c,d
# res=add(5,6)
# print(res)
# output:
# (11, -1)
# def add(x,y):
#     c=x+y
#     return
# res=add(5,6)
# print(res)
# output:
# none
# def add(x,y):
#     pass
# res=add(5,6)
# output:
# it is executed but it does not display any output.(blank)
# def add(x,y):
#     return(x+y)
# print(add(23,12))
# print(add(2,4))
# output:
# 35
# 6
# def add(x,y):
#     res=add(5,6)
# def add(x,y):
#     pass
# res=add(5,6)
# print(res)
# def add(x,y):
#     sum=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     print(sum, sub,mul,div)
# a=add(10,5)

# def add(x,y):
#     c=x+y
#     return c
# print(add('ab','cb'))
# output:
# abcb
# def add(x,y):
#     pass
#     a=x+y
#     print(a)
# add(10,5)
# output:
# 15
# def f1():
#     print("hello")
# f1()
# print(f1())
# output:
# hello
# hello
# def func(x,w=10,*y,**z):
#     print(x)
#     print(y)
#     print(z)
#     print(w)
# func(1,2,3,4,5,56,k1=4,k2=5,k3=10)
# output:
# 1
# (3, 4, 5, 56)
# {'k1': 4, 'k2': 5, 'k3': 10}
# 2
# def add(x,y):
#     c=x+y
# res=add(10,5)
# print(res)
# output:
# none
# def my_function():
#     print("Hello from a function")
# my_function()

# def my_function(fname):
#     print(fname+ "reference")
# my_function("java")
# my_function("python")
# my_function("unix")

# def my_function(fname,lname):
#     print(fname+ " " +lname)
# my_function("bhargavi","thota")

# def my_function(fname,lname):
#     print(fname+ " "+lname)
# my_function("rakesh")

# def my_function(*kids):
#     print("The younger child is " +kids[2])
# my_function("rakesh","bhargavi","vasudha")
#keyword arguments:
# def my_function(child1,child2,child3):
#     print("The younger child is " +child3)
# my_function(child1="emil",child2="tobias",child3="linus")

# def my_function(**kid):
#     print("His last name is "+kid["lname"])
# my_function(fname="emil",lname="refnes")
#Default argument:
# def my_function(country="norway"):
#     print("Iam from " +country)
# my_function("sweden")
# my_function("india")
# my_function("brazil")
# my_function()
#Return values
# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

#pass statement
# def my_function():
#     pass

#without arguments and without return values
# def addition():
#     a,b=5,7
#     c=a+b
#     print(c)
# addition()

#without arguments with return values
# def substraction():
#     a,b=25,15
#     s=a-b
#     return s
# print(substraction())

#with arguments without return values
# def multi(a,b):
#     s=a*b
#     print(s)
# multi(10,5)

#with arguments with return values
# def division(a,b):
#     s=a/b
#     return s
# print(division(50,10))
#Regular Expressions
# import re
# txt="The rain in spain"
# x=re.search("^The.*spain$",txt)
# if x:
#     print("match")
# else:
#     print("no match")
# import re
# txt = "The rain in Spain"
# x = re.findall("[^arn]", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# output:
# ['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']
# Yes, there is at least one match!
# import re
# print(re.match('^s','sai'))
# output:
# <re.Match object; span=(0, 1), match='s'>
# import re
# print(re.match('..i','sai'))
# output:
# <re.Match object; span=(0, 3), match='sai'>
# import re
# print(re.match('^[a-i].i$','sai'))
# output:
# None
# import re
# print(re.match('^[A-Z].i$','Sai'))
#overloading
# def add(a, b):
#     return a + b
# def add(a, b, c):
#     return a + b + c
# add(2, 3)
#Datetime module
# import datetime
# x=datetime.datetime.now()
# print(x)
# output:
# 2021-03-17 00:39:35.666210
# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))
# output:
# 2021
# Wednesday
# from datetime import datetime,timedelta
# x=datetime.now()
# y=x+timedelta(45)
# print(y)
# output:
# 2021-05-01 01:37:01.357619
# from datetime import datetime,timedelta
# x=datetime(2021,3,18)
# y=x+timedelta(days=12)
# print(y)
# output:
# 2021-05-02 00:00:00
# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%c"))
# output:
# Wed Mar 17 02:02:25 2021
# import datetime
# x = datetime.datetime.now()
# print(x.hour,x.minute,x.second)
# import datetime
# x = datetime.datetime.now()
# print(x.strftime("%X"))
# output:
# 14:40:36
# from datetime import datetime
# date="2020-06-19 02:43:54"
# x=datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
# print(x)
# from datetime import datetime
# now=datetime.now()
# now.strftime("%Y-%m-%d,%H:%M:%S")

# from datetime import datetime
# date_time_str = '18/09/19 01:55:19'
# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
# print("The type of the date is now",  type(date_time_obj))
# print("The date is", date_time_obj)
# from datetime import datetime
# datestr="17/03/21 02:56:43"
# date=datetime.strptime(datestr,'%d/%m/%y %H:%M:%S')
# print(date)
# output:
# 2021-03-17 02:56:43
#fibonacci series
# a=0
# b=1
# c=0
# n=int(input("enter the value:"))
# for i in range(1,n+1):
#     a=b
#     b=c
#     c=a+b
#     print(b,end=" ")
# output:
# enter the value:6
# 0 1 1 2 3 5
#palindrome or not
# num=int(input("enter n value:"))
# rev=0
# temp=num
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num/10
# if(num==rev):
#     print("palindrome")
# else:
#     print("not palindrome")
#String palindrome
# s=input("enter the string:")
# x=s[::-1]
# if s==x:
#     print("palindrome")
# else:
#     print("not palindrome")
# output:
# enter the string:dad
# palindrome
#Method resolution order(MRO)
# class A:
#     def rk(self):
#         print(" In class A")
# class B:
#     def rk(self):
#         print(" In class B")
# class C(A, B):
#     def __init__(self):
#         print("Constructor C")
# r = C()
# print(C.__mro__)
# print(C.mro())
# output:
# Constructor C
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# Python program to check if the number is an Armstrong number or not
#Armstrong number
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum+=digit ** 3
#    temp//= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

# list=[10,100,43,56,78]
# list.sort()
# print(list[-2])















