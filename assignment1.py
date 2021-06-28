# Task1:
# s="Tweak Talent Technologies"
# print(len(s))
#output:25

# Task2:
# s="6"
# a=int(s)
# b=float(s)
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# output:\
# 6
# 6.0
# <class 'int'>
# <class 'float'>
# Task3:
# x={'hai':3,'hello':5,'welcome':7}
# li=list(x)
# print(li)
# output:['hai', 'hello', 'welcome']
# Task4:
# li=[1,2,3,4]
# t=tuple(li)
# print(t)
# print(list(t))
# output:
# (1, 2, 3, 4)
# [1, 2, 3, 4]

# Task5:
# dict={'jan':1,'feb':'2','mar':3,'apr':5}
# dict.update({'apr':4})
# print(dict)
# output:
# {'jan': 1, 'feb': '2', 'mar': 3, 'apr': 4}

# task6:
# li=[5,3,9,2,7,8]
# tp=(2,4,1,8,5,6)
# print(li)
# print(tp)
# print(li.__sizeof__())
# print(tp.__sizeof__())
# li.insert(2,6)
# print(li)
# li[2]=6
# print(li)
# tp[3]=7
# print(tp)
# output:
# [5, 3, 9, 2, 7, 8]
# (2, 4, 1, 8, 5, 6)
# Traceback (most recent call last):
#   File "C:\Users\BHARGAVI\PycharmProjects\pythonProject1\assignment1.py", line 51, in <module>
#     tp[3]=7
# TypeError: 'tuple' object does not support item assignment
# 136
# 72
# [5, 3, 6, 9, 2, 7, 8]
# [5, 3, 6, 9, 2, 7, 8]
#

# Task7:
# a='welcome to python'
# print(a[4:10])
# output:ome to
# Task8:
# a=input("Enter the string:")
# print(a[-1::-1])
# output:
# Enter the string:hello
# olleh

# Task9:
# li=[10,5,4,20,1,15,12]
# li.sort()
# print(li)
# output:
# [1, 4, 5, 10, 12, 15, 20]
# Task10:
# list=[x for x in range(10)]
# print(list)
# dict={x:x for x in range(10)}
# print(dict)
# output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
# Task11:
# list=["Technologies","Talent","Tweak"]
# list.reverse()
# print(list)
# output:
# ['Tweak', 'Talent', 'Technologies']
# Task12:
# print([i for i in range(1,30) if i%2==0])
# output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# Task13:
# l1=['a','b','c']
# l2=[1,2,3]               #using zip()
# d=dict(zip(l1,l2))
# print(d)
# output:
# {'a': 1, 'b': 2, 'c': 3}
# Task14:
# li = list()
# for i in range(1, 31):
#     li.append(i ** 2) # using append() and print the first and last characters  used slicing
# print(li[0:5])
# print(li[-5:])
# output:
# [1, 4, 9, 16, 25]
# [676, 729, 784, 841, 900]

# task15:
# l=[1,2,5,54,6,12,17]
# number=int(input())
# index_number=int(input())
# l.index(number,index_number)

#
# task16:
# n=int(input("enter the number:"))
# list1=["welcome","to","python"]
# list2=[]
# for word in list1:
#     if len(word)>=n:
#         list2.append(word)
# print(list2)
# output:
# enter the number:3
# ['welcome', 'python']

#task17:
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}  # using update() and combine the three dictionaries
# dict1.update(dict2)
# dict1.update(dict3)
# print(dict1)
# output:
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# task18:
# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# print("1.add 2.sub 3.mul 4.div 5.mod. 6.power 7.floor 8.comparision 9.logical 10.membership")
# choice=int(input("Enter the choice:"))
# if choice==1:
#     print("add is",a+b)
# elif choice==2:
#     print("sub is",a-b)
# elif choice==3:
#     print("mul is",a*b)
# elif choice==4:
#     print("div is",a/b)
# elif choice==5:
#     print("modular division is",a%b)
# elif choice==6:
#     print("power is",a^b)
# elif choice==7:
#     print("floor is",a//b)
# elif choice==8:
#     a=33
#     b=33
#     if b>a:
#         print("b is greater than a")
#     elif a==b:
#         print("a is equal to b")
# elif choice==9:
#     a=330
#     b=33
#     c=500
#     if a>b and c>a:
#         print("Both conditions are true")
# elif choice==10:
#     a=[1,2,3,4]
#     b=[4,5,6,7]
#     print(4 in a)
#     print(a not in b)
# else:
#     print("Invalid choice")
# output:
# enter a value:2
# enter b value:5
# 1.add 2.sub 3.mul 4.div 5.mod. 6.power 7.floor 8.comparision 9.logical 10.membership
# Enter the choice:4
# div is 0.4

#task19:
# li=[1,1,2,3,4,3,2,4,5]
# print(set(li))
# output:
# {1, 2, 3, 4, 5}
# task20:
# dict={'jan':1,'feb':'2','mar':3,'apr':5}
# if 'may' in dict:
#     print("It is in dictionary")
# else:
#     print("It is not in dictionary")
#
# output:
# It is not in dictionary

# li1=['k','e','t','h','a']
#li=''
# print(''.join(li1))
# output:
# ketha

# name='ketha'
# data=list(name)
# print(data)
# input='bhargavi'
# x=[c for c in input]
# print(x)
# output:
# ['b', 'h', 'a', 'r', 'g', 'a', 'v', 'i']
# x='re'
# y=x*2
# z='java'
# print(z+y)
# output:
# javarere
# a={'b':19,'a':9,'c':12}
# print(sorted(a))
# output:
# ['a', 'b', 'c']
# x=int(input())
# y=[c for c in range(x) if c%2==0]
# print(y)
# output:
# 10
# [0, 2, 4, 6, 8]
# tuple=(3,1,5,8)
# print(sorted(tuple))
# output:
# [1, 3, 5, 8]
# x=tuple(enumerate([1,2,3,4]))
# print(x)
# output:
# ((0, 1), (1, 2), (2, 3), (3, 4))

# x={'abc','cds','grd','gft'}
# y=x.pop()
# print(y)
# print(x)
# output:
# grd
# {'cds', 'gft', 'abc'}

# list=[x if x%2==0 else x*100 for x in range(1,10)]
# print(list)
# output:[100, 2, 300, 4, 500, 6, 700, 8, 900]

# list=[x*50 if x%2!=0 else x*100 for x in range(1,10) ]
# print(list)
# output:50, 200, 150, 400, 250, 600, 350, 800, 450]

# x="save the trees"
# print(x.replace(' ','**',2))
# output:
# save**the**trees
# a={1,2,3,4,5,6,7,8,9,76,36,367}
# a.pop()
# print(a)
#output:
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 36}

# a={1,2,3,4,5,6,7,8,9,76,36,367}
# x=a.pop()
# print(x)
# output:
# 1

# x=[1,3,5,6,9,7,16,98,21,10,80]
# x.pop()
# print(x)   # pop the last element in list
# output:
# [1, 3, 5, 6, 9, 7, 16, 98, 21, 10]

# x=[1,3,5,6,9,7,16,98,21,10,80]
# a=x.pop()
# print(a)
# output:
# 80

# x={4,3,6,98,2,12,56}
# x.remove(12)
# print(x)
# output:
# {2, 3, 4, 98, 6, 56}

# x={4,3,6,98,2,12,56}
# x.remove(33)
# print(x)
# output:
# Traceback (most recent call last):
#   File "C:\Users\BHARGAVI\PycharmProjects\pythonProject1\assignment1.py", line 298, in <module>
#     x.remove(33)
# KeyError: 33

# x={34,54,23,65,98,10}
# x.discard(23)
# print(x)
# output:
# {65, 34, 98, 54, 10}

# x={34,54,23,65,98,10}
# x.discard(100)
# print(x)
# output:
# {65, 34, 98, 54, 23, 10}

# test=[{'name':'gang','age':37},{'name':'ravi','age':31}]
# test1=[{'name':'mahesh','age':32}]
# test.append(test1)
# print(test)
# test=[{'name':'gang','age':37},{'name':'ravi','age':31}]
# test1=[{'name':'mahesh','age':32}]
# test.extend(test1)
# print(test)

# def Test(x):
#     i=0
#     while i<len(x):
#         print(str(i) + ',' + x[i])
#         i=i+1
# colors=['red','green','yellow','blue']
# Test(colors)
#output:
# 0,red
# 1,green
# 2,yellow
# 3,blue

#
# def Test(x):
#     i=1
#     for y in x:
#         print(i, ',' ,y)
#         i=i+1
# colors = ['red', 'green', 'yellow', 'blue']
# Test(colors)

# colors=['red','blue','green','yellow']
# print(list(enumerate(colors)))