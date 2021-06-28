#Task1:
# d={'a':'b','b':'c','c':'a'}
# l1=[]
# s=input("enter the values:")
# for i in s:
#     if i in d.keys():
#         l1.append(d[i])
# print("".join(l1))
# #output:
# enter the values:abc
# bca
#Task2:
# i=1
# fact=1
# while i<=5:
#     fact=fact*i
#     i=i+1
# print(fact)
#output:
# 120
#Task3:
# l=[22,11,2,5,27,10,55]
# maxvalue=l[0]
# minvalue=l[0]
# for i in l:
#     if i>=maxvalue:
#         maxvalue=i
#     if i<=minvalue:
#         minvalue=i
# print(maxvalue,minvalue)
# output:
# 55 2
#Task4:
# n=int(input("enter the marks:"))
# if n>90:
#     print("A+ Grade")
# elif n>70 and n<=90:
#     print("A Grade")
# elif n>50 and n<=70:
#     print("B Grade")
# elif n>35 and n<=50:
#     print("C Grade")
# else:
#     print("fail")
# #output:
# enter the marks:95
# A+ Grade
#Task5:
# list=[0,1,2,3,4,6,7]
# l1=list[1:7]
# l2=[]
# for i in l1:
#     if i%2==0:
#         l2.append("even")
#     else:
#         l2.append("odd")
# print(l2)
# output:
# ['odd', 'even', 'odd', 'even', 'even', 'odd']
#Task6:
# def sum():
#     sum=0
#     for i in range(1,21):
#         if i%3==0 or i%5==0:
#             print(i)
#             sum=sum+i
#     print("sum of 3 and 5 multiples are:",sum)
# sum()
# output:
# 3
# 5
# 6
# 9
# 10
# 12
# 15
# 18
# 20
# sum of 3 and 5 multiples are: 98
#Task7:
# i=1
# n=5
# while i<=n:
#     print(i*'*')
#     i+=1
# output:
# *
# **
# ***
# ****
# *****
#Task8:
# def fizz_buzz(n):
#     if n%3==0 and n%5==0:
#         return "fizz-Buzz"
#     elif n%3==0:
#         return "fizz"
#     elif n%5==0:
#         return "buzz"
#     else:
#         return n
# print(fizz_buzz(15))
#output:fizz-buzz
#Task9:
# s="India is my country"
# words = s.split(' ')
# print(words)
# rev= ' '.join(reversed(words))
# print(rev)
# print(rev[-1::-1])
#output:
#['India', 'is', 'my', 'country']
# country my is India
# aidnI si ym yrtnuoc

#Task10:
# dict={i:v for i,v in enumerate([1,2,3,4,5])}
# print(dict)
# output:
# {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
#Task11:
# def even(x):
#     if x%2==0:
#         print("Even number")
#     else:
#         print("odd number")
# even(62)
#output:Even number
#Task12:
# def vote(x):
#     if x>=18:
#         print("You are eligible for vote")
#     else:
#         print("you are not eligible for vote")
# vote(17)
#output:
#You are not eligible for vote
#Task13:
# def perfect(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum=sum+i
#     if sum==n:
#         print(sum)
# n = int(input("enter n value:"))
# for x in range(1,n+1):
#     perfect(x)
# output:
# enter n value:1000
# 6
# 28
# 496
#Task14:
# li=[20,32,33,41,88,17,18,7]
# even_list=list(filter(lambda x:x%2==0,li))
# print(even_list)
# odd_list=list(filter(lambda x:x%2!=0,li))
# print(odd_list)
# output:
# [20, 32, 88, 18]
# [33, 41, 17, 7]
#Task15:
# l=[2,3,4,5,6,7]
# list1=list(map(lambda n:n*10,l))
# print(list1)
# output:
# [20, 30, 40, 50, 60, 70]
#Task16:
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(factorial(8))
#output:40320
#Task17:
# def leapyear(year):
#     if(year%4==0 or ((year%400==0) and (year%100!=0))):
#         print("leap Year")
#     else:
#         print("not leap year")
# leapyear(2020)
# output:Leap Year
#Task18:
# def dynamic(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# dynamic(1,2,3,4,5,6)
#Task19:
# def my_func(d):
#     for (k,v) in d.items():
#         print("key:",k,"value:",v)
# my_func({'a':1,'b':2,'c':3})
# output:
# key: a value: 1
# key: b value: 2
# key: c value: 3
#Task20:
# n=1
# f1=False
# while n>=1:
#     print(n*'*')
#     if n==5:
#         f1=True
#     if f1:
#         n-=1
#     else:
#         n+=1
# output:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *










