#Task1:
# n=5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if i==3 and j==n:
#             print("* ", end="")
#     print(" ")
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print("* ", end="")
#     print(" ")
# output:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#Task1(2nd method)
# n=int(input("enter the value:"))
# for i in range(1,n+1):
#     print(i*'*')
# for j in range(1,n):
#     n=n-1
#     print(n*'*')
#Task1(using file handling)
# f=open("python.txt","a")
# n=int(input("enter the value:"))
# for i in range(n+1):
#     f.write(i*'*')
#     f.write('\n')
# for j in range(n):
#     n=n-1
#     f.write(n*'*')
#     f.write('\n')
# f.close()
#Task2:
# x=5
# y=0
# try:
#     print(x/y)
# except Exception as e:
#     print(e)
# else:
#     print("else")
# finally:
#     print("Finally method")
# output:
# division by zero
# Finally method
#Task3:
#zeroDivisionError
# n=int(input("enter n value:"))
# print(n/0)
#NameError
# def func():
#     print(ans)
# func()
#IndexError
# list=[1,3,5]
# print(list[3])
#KeyError
# dict={'a':1,'b':3,'c':5}
# print(dict['d'])
#EOFError
# while True:
#     data = input('Enter name : ')
#     print ('Hello',data)
#AttributeError
# class Attributes(object):
#     pass
# object = Attributes()
# print(object.attribute)
#Task4:
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
# output:
# Enter your age:18
# He is not eligible
#Task5:
# f=open("python.txt","x")
# f=open("python.txt",'w')
# f.write("Hai,This is python")
# f=open("python.txt","r")
# print(f.read())
# f=open("python.txt","a")
# f.write("\npython is the best")
# f.close()
# output:
# WrteMode:This is python
# Read Mode:Hai,This is python
# append Mode:python is the best
#Task6:
# def longestword():
#     with open('python.txt', 'r') as f:
#               words = f.read().split()
#     maxlen = len(max(words, key=len))
#     if maxlen>10:
#         return [word for word in words if len(word) == maxlen]
# print(longestword())
#output:
# ['developingg']
#Task7:
# f=open("python.txt","r")
# dict={}
# words=f.read().split()
# for i in words:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
#       (or)
# from collections import Counter
# f=open("python.txt","r")
# words=f.read().split()
# print(Counter(words))
# output:
# Counter({'India': 2, 'is': 2, 'country.': 2, 'my': 1, 'a': 1, 'well': 1, 'developingg': 1})
#Task8:
# with open("python.txt","a",encoding='utf8') as f:
#     f.write("\n El Niño")
#Task9:
# from practice import*
# add(10,24)
# sub(12,10)
# output:
# 34
# 2
#Task10:
# import math
# print("The value of pi is", math.pi)
# import sys
# print(sys.path)
# from practice import mul,div
# mul(12,5)
# div(12,3)
# output:
# The value of pi is 3.141592653589793
# 60
# 4.0
#Task11:
# s="google.com"
# dict={}
# for i in s:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
#print(dict)
# output:{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#Task12:

#Task13:
# from functools import reduce
# print(reduce(lambda x,y:x+y,[5,10,15,20]))
#output:
#50
#Task14:
# list=['abc', 'xyz', 'aba', '1221']
# count=0
# for i in list:
#     if len(i)>1 and i[0]==i[-1]:
#         count=count+1
# print("The count is",count)
# output:
# The count is 2
#Task15:
# list=['a', 'b', 'c', 'a', 'd', 'e']
# dict={}
# for i in list:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
# output:
# {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
#Task16:
# dict={'a':10,'b':2,'c':5,'d':4}
# value=1
# for i in dict.values():
#     value=value*i
# print(value)
# output:
# 400
#Task17:
# dict={'a':12,'b':20,'c':50,'d':45}
# x=dict.values()
# max=max(x)
# min=min(x)
# print("maximum number is:",max)
# print("Minimum number is:",min)
# output:
# maximum number is: 50
# Minimum number is: 12
#Task18:
# x=int(input("Enter x Value:"))
# y=int(input("Enter y Value:"))
# z=int(input("Enter z Value:"))
# a1 = min(x, y, z)
# a3= max(x, y, z)
# a2 = (x + y + z) - a1 - a3
# print("sorted order is:", a1, a2, a3)
#         (or)
# list=[x,y,z]
# list.sort()
# print(list)
# output:
# Enter x Value:30
# Enter y Value:23
# Enter z Value:10
# sorted order is: 10 23 30
#Task19:
# a=int(input("Enter a Value:"))
# b=int(input("Enter b Value:"))
# li=[a,b]
# li[0]=li[1]
# print(li)
#output:
# Enter a Value:25
# Enter b Value:50
# [50, 50]
#Task20:
# def sum(x,y,z=10):
#     sum=x+y+z
#     print("sum of x,y,z is:",sum)
# sum(50,30,5)
# output:
# sum of x,y,z is: 85
#Task21:
# def test(*args,**kwargs):
#     print(kwargs)
#     kwargs.update(k3=7)
#     print(kwargs)
#     print(args)
# test(10,20,30,k1=5,k2=6,k3=8)
#output:
# {'k1': 5, 'k2': 6, 'k3': 8}
# {'k1': 5, 'k2': 6, 'k3': 7}
# (10, 20, 30)
#Task22,23:
# class Arithmetic:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def addition(self):
#         return self.x+self.y
#     def substraction(self):
#         return self.x-self.y
# class Calculator(Arithmetic):
#     def multiplication(self):
#         return self.x*self.y
#     def moddivision(self):
#         return self.x%self.y
# class FloatDiv(Calculator):
#     def floatdivision(self):
#         return self.x/self.y
# obj=FloatDiv(10,2)
# print("The addition of x,y is:",obj.addition())
# print("The substraction of x,y is:",obj.substraction())
# print("The multiplication of x,y is:",obj.multiplication())
# print("The modular division of x,y is:",obj.moddivision())
# print("The Float division of x,y is:",obj.floatdivision())
# output:
# The addition of x,y is: 12
# The substraction of x,y is: 8
# The multiplication of x,y is: 20
#The modular division of x,y is: 0
#The Float division of x,y is: 5.0
#Task24:
#Multiple inheritance
# class Arithmetic:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def addition(self):
#         return self.x+self.y
#     def substraction(self):
#         return self.x-self.y
# class Calculator():
#     def addition(self):
#         return self.x+self.y
#     def substraction(self):
#         return self.x-self.y
# class Floatdiv(Arithmetic,Calculator):
#     def multiplication(self):
#         return self.x*self.y
# obj=Floatdiv(20,10)
# print("The addition of x,y is:",obj.addition())
# print("The substraction of x,y is:",obj.substraction())
# print("The multiplication x,y is:",obj.multiplication())
# output:
# The addition of x,y is: 30
# The substraction of x,y is: 10
# The multiplication x,y is: 200
#@multilevel inheritance
# class Arithmetic:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def addition(self):
#         return self.x+self.y
#     def substraction(self):
#         return self.x-self.y
# class Calculator(Arithmetic):
#     def multiplication(self):
#         return self.x*self.y
#     def moddivision(self):
#         return self.x%self.y
# class FloatDiv(Calculator):
#     def floatdivision(self):
#         return self.x/self.y
# obj=FloatDiv(50,25)
# print("The addition of x,y is:",obj.addition())
# print("The substraction of x,y is:",obj.substraction())
# print("The multiplication of x,y is:",obj.multiplication())
# print("The modular division of x,y is:",obj.moddivision())
# print("The Float division of x,y is:",obj.floatdivision())
# output:
# The addition of x,y is: 75
# The substraction of x,y is: 25
# The multiplication of x,y is: 1250
# The modular division of x,y is: 0
# The Float division of x,y is: 2.0
#Task25:
# f=open("test.txt","w")
# f.write("welcome to Tweak Talent Technologies")
# f.close()
# output:
# Using writemode automatically create test.txt file and insert the data same time.
#Task26:
# with open("python.txt","a",encoding='utf8') as f:
#     f.write("\n Dejan Živković','Gregg Berhalter','James Stevens','Mike Windischmann' ,'Gunnar Heiðar Þorvaldsson")
# f=open("python.txt","r")
# print(f.read())
# output:
# India is my country.
# India is a well developingg country.
#  Dejan Å½ivkoviÄ‡','Gregg Berhalter','James Stevens','Mike Windischmann' ,'Gunnar HeiÃ°ar Ãžorvaldsson

#Task27:
# f=open("python.txt","w")
# f.write("India is my country")   without context processor
# f.close()
# with open("python.txt","r") as f:  With context processor
#     print(f.read())
# output:
# ReadMode:India is my country
#Task28:
# try:
#     print(x)
#     print(10/0)
# except ZeroDivisionError  as e:
#     print("zero division error statement")
# except NameError as e:
#     print("Name error statement")
# finally:
#     print("finally block")
# output:
# Name error statement
# finally block
#Task29:
# class Validate(Exception):
#     pass
# n=int(input("Enter a value:"))
# try:
#

#Task30:
#@filter
# print(list(filter(lambda x:x>10,[12,3,5,6,43,23])))
# output:
# [12, 43, 23]
#@map
# li=list(map(lambda n:n*n,[2,3,4,5,6]))
# print(li)
# output:
# [4, 9, 16, 25, 36]
#@reduce
# from functools import reduce
# print(reduce(lambda x,y:x+y,[2,3,6,1,9,5,3]))
# output:
# 29
#Task31:
# list=[1,0,1,2,0,1,0,2]
# seggrigate=([x for x in list if x==0] + [x for x in list if x==1]+[x for x in list if x==2])
# print(seggrigate)
# (or)
# list=[1,0,1,2,0,1,0,2]
# list.sort()
# print(list)
# output:
# [0, 0, 0, 1, 1, 1, 2, 2]
#Task32:
# f=open("python.txt","r")
# words=f.read().split()
# x=set(words)
# print(x)
# output:
# {'India', 'country.', 'a', 'well', 'developed', 'is', 'my'}
#Task33:
# def decor(func):
#     def inner(age):
#         if age>=18:
#             print("He is  eligible")
#         else:
#             func(age)
#     return inner
# @decor
# def vote(age):
#     print("hello,you are not eligible")
# vote(age = int(input("enter the age:")))
#output:
# enter the age:12
#hello,you are not eligible
#Task35:
# def factorial(func):
#     def inner(n):
#         from functools import reduce
#         print(reduce(lambda x,y:x*y,n))
#         func(n)
#     return inner
# @factorial
# def fact(n):
#     print("Hello,factorial")
# fact(range(1,7))
# output:
# 720
# Hello,factorial
#Task38:
# from threading import*
# import time
# class Factorial:
#     def m1(self):
#         fact=1
#         for i in range(1,6):
#             fact=fact*i
#             time.sleep(1)
#             print(fact)
# obj=Factorial()
# t=Thread(target=obj.m1)
# t.start()
# time.sleep(2)
# t.join()
# fact=1
# for i in range(1,6):
#     fact=fact*i
#     time.sleep(1)
#     print(fact)
# output:
# 1
# 2
# 6
# 24
# 120
# 1
# 2
# 6
# 24
# 120
#Task39:
# from multiprocessing import*
# import time
# class Factorial:
#     def m1(self):
#         fact=1
#         for i in range(1,6):
#             fact=fact*i
#             time.sleep(1)
#             print(fact)
# obj=Factorial()
# if __name__ == '__main__':
#     p=Process(target=obj.m1)
#     p1=Process(target=obj.m1)
#     p.start()
#     time.sleep(2)
#     p.join()
#     p1.start()
#     p1.join()
# #output:
# 1
# 2
# 6
# 24
# 120
# 1
# 2
# 6
# 24
# 120
#Task40:
# class Arithmetic():
#     def add(self,x,y):
#         print(x+y)
#     @classmethod
#     def sub(cls,x,y):
#         print(x-y)
#     @staticmethod
#     def mul(x,y):
#         print(x*y)
# obj=Arithmetic()
# obj.add(10,20)
# Arithmetic.sub(20,10)
# Arithmetic.mul(10,20)
# obj.mul(2,3)
# output:
# 30
# 10
# 200
# 6


































