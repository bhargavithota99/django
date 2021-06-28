# Task1:
# d = {1:['a', 'G', 'k', 'l'], 2:['G', 'b', 'c'], 3:['a', 'k', 'G', 'c']}
# n=input("Enter the character:")
# count=0
# for i in d.values():
#     if n in i:
#         count=count+1
# print(count)
# Task2:
# list=['Red','Green','White','Black','Pink','Yellow']
# list1= [x for (i,x) in enumerate(list) if i not in (0,4,5)]
# print(list1)
# output:['Green', 'White', 'Black']
# Task3:
# def count(values):
#     count= 0
#     for i in values:
#         if len(i)>1 and i[0] ==i[-1]:
#             count+= 1
#     return count
# print(count(['abc', 'xyz', 'aba', '1221']))
# output:2
# Task4:
# s="google.com"
# dict={}
# for i in s:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
# output:{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# Task5:
# d = {"name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}
# keys=['name','salary']
# dict={k:d[k] for k in keys}
# print(dict)
# output:{'name': 'Kelly', 'salary': 8000}
#
# Task6:
# n=55
# dict={'apple':55,'banana':6,'tomato':7,'grapes':4}
# print(n in dict.values())
# output:True
# Task7:
# from functools import reduce
# print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))
# output:21
# Task8:
# li=[1,2,3,2,4,5,6,5,1,7]
# print(list(set(li)))
#     (or)
# li=[1,2,3,2,4,5,6,5,1,7]
# list=[]
# for i in li:
#     if i not in list:
#         list.append(i)
# print(list)
# output:[1, 2, 3, 4, 5, 6, 7]
# Task9:
# dict={'a':10,'b':5,'c':10}
# value=1
# for i in dict:
#     value=value*dict[i]
# print(value)
# output:500
# Task10:
# s={24,65,45,72,82,48,11,5}
# s.remove(65)
# print(s)
# s.discard(45)
# print(s)
# s.remove(55)
# print(s)
# s.discard(90)
# print(s)
# output:
# traceback (most recent call last):
#   File "C:\Users\BHARGAVI\PycharmProjects\pythonProject1\assignment2.py", line 54, in <module>
#     s.remove(55)
# KeyError: 55
# {5, 72, 11, 45, 48, 82, 24}
# {5, 72, 11, 48, 82, 24}
#
# Task11:
# n=int(input("Enter the number:"))
# i=1
# while i<=n:
#     print(i)
#     i=i+1
# output:
# Enter the number:5
# 1
# 2
# 3
# 4
# 5
#
# Task12:
# n=int(input("enter number1:"))
# for i in range(1,11):
#     print(n,'*',i,'=',n*i)
# output:
# enter number1:5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
# Task13:
# list1=[12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# for x in list1:
#     if x>150:
#         break
#     if x%5==0:
#         print(x)
# output:
# 15
# 55
# 75
# 150
# Task14:
# list=[50,40,30,20,10]
# for i in range(len(list)-1,-1,-1):
#     print(i)
# output:
# 10
# 20
# 30
# 40
# 50
#
# Task15:
# n=int(input("Enter the value:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
# output:
# Enter the value:6
# 720
# Task16:
# list= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(1,len(list),2):
#     print(list[i])
# output:
# 20
# 40
# 60
# 80
# 100

# Task17:
# n=input("enter the number:")
# count=0
# for i in n:
#     count=count+1
# print("count is",+count)
# output:
# enter the number:123
# count is 3
# Task18:
# dict={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
# print(dict['class']['student']['marks']['history'])
# output:80
# Task19:
# def product(val1,val2):
#     mul=val1*val2
#     if mul>1000:
#         sum=val1+val2
#         print(sum)
#     else:
#         print(mul)
# product(10,200)
# output:210
#
# Task20:
# n=input("enter the string:")
# print(n[0::2])
# output:
# enter the string:tweaktalenttechnologies
# tekaetehoois
