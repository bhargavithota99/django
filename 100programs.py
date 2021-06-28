# Task1:
# l=[]
# for i in range(2000, 3201):
#    if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print(','.join(l))
# Task2:
# n=int(input("enter a value:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
# Task3:
# n=int(input("enter input:"))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)
# Task4:
# n=input('enter values')
# l=n.split(',')
# t=tuple(l)
# print(l)
# print(t)
# Task5:
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = input("enter a string:")
#
#     def printString(self):
#         print(self.s.upper())
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
# Task6:
# import math
# c=50
# h=30
# value = []
# n=input('enter values')
# items=[x for x in n.split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))
# Task7:
# n =input('Enter values:')
# dimensions=[int(x) for x in n.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
# print(multilist)
# Task8:
# n=input('enter the strings:')
# items=[x for x in n.split(',')]
# items.sort()
# print(','.join(items))
# Task9:
# lines = []
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
# for sentence in lines:
#     print(sentence)
# Task10:
# s =input()
# words = [word for word in s.split(" ")]
# print(" ".join(sorted(list(set(words)))))
# Task11:
# n=input()
# value = []
# items=[x for x in n.split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)
# print(','.join(value))
# Task12:
# values = []
# for i in range(1000, 3001):
#     s=str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))
# Task13:
# s =input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])
# Task14:
# s =input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"])
# print ("LOWER CASE", d["LOWER CASE"])
# Task15:
# a =input('enter a value:')
# n1 = int("%s" % a)
# n2 = int("%s%s" % (a,a))
# n3 = int("%s%s%s" % (a,a,a))
# n4 = int("%s%s%s%s" % (a,a,a,a))
# print(n1+n2+n3+n4)
# Task16:
# values =input('enter the numbers:')
# numbers = [x for x in values.split(",") if int(x)%2!=0]
# print( ",".join(numbers))
# Task17:
# netAmount = 0
# while True:
#     s=input()
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print(netAmount)
# Task18:
# import re
# value = []
# n=input('enter passwords:')
# items=[x for x in n.split(',')]
# for p in items:
#     if len(p)<6 or len(p)>12:
#         continue
#     else:
#         pass
#     if not re.search("[a-z]",p):
#         continue
#     elif not re.search("[0-9]",p):
#         continue
#     elif not re.search("[A-Z]",p):
#         continue
#     elif not re.search("[$#@]",p):
#         continue
#     # elif re.search("\s",p):
#     #     continue
#     else:
#         pass
#     value.append(p)
# print(",".join(value))
# Task19:
# from operator import itemgetter, attrgetter
# l = []
# while True:
#     s =input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))
# print(sorted(l, key=itemgetter(0,1,2)))
# Task20:
# def putnumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j
# for i in putnumbers(100):
#     print(i)
# Method:2
# class iterator(object):
#    def __init__(self, n):
#        super(iterator, self).__init__()
#         self.n = n
#     def divBySeven(self):
#         for i in range(0, self.n):
#             if i % 7 == 0:
#                 yield i
# for num in iterator(100).divBySeven():
#     print(num)
# Task21:
# import math
# pos = [0,0]
# while True:
#     s=input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
# print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
# Task22:
# freq = {}
# line =input('Enter the sentence:')
# for word in line.split():
#     freq[word] = freq.get(word,0)+1
# words = sorted(freq.keys())
# for w in words:
#     print("%s:%d" % (w,freq[w]))
# Task23:
# def square(num):
#     return num ** 2
# print(square(5))
# print(square(8))
# Task24:
# print(abs.__doc__)
# print(int.__doc__)
# print(input.__doc__)
# def square(num):
#     return num ** 2
# print(square(2))
# print(square.__doc__)
# Task25:
# class Person:
#     name = "Person"
#     def __init__(self, name=None):
#         self.name = name
# girl= Person("Bhargavi")
# print("%s name is %s" % (Person.name,girl.name))
# boy= Person("Rakesh")
# print("%s name is %s" % (Person.name, boy.name))
# Task26:
# def Sum(num1, num2):
# 	return num1+num2
# print(Sum(18,22))
# Task27:
# def printValue(n):
# 	print(str(n))
# printValue(10)
# Task28:
# def printValue(s1,s2):
# 	print(int(s1)+int(s2))
# printValue("25","45")
# Task29:
# def printValue(s1,s2):
# 	print(s1+s2)
# printValue("11-06","-98")
# Task30:
# def printValue(s1, s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1 > len2:
#         print(s1)
#     elif len2 > len1:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# printValue("Bhargavi", "Rakesh")
# Task31:
# def evenoradd(n):
#     if n%2==0:
#         print("It is an even number")
#     else:
#         print("It is an odd number")
# evenoradd(6)
# Task32:
# def printDict():
#     d = dict()
#     d[1]=1
#     d[2]=2**2
#     d[3]=3**2
#     d[4]=4**2
#     print(d)
# printDict()
# Task33:
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     print(d)
# printDict()
# Task34:
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     for (k, v) in d.items():
#         print(v)
# printDict()
# Task35:
# def printDict():
#     d = dict()
#     for i in range(1, 21):
#         d[i] = i ** 2
#     for k in d.keys():
#         print(k)
# printDict()
# Task36:
# def printList():
#     li = list()
#     for i in range(1, 21):
#         li.append(i ** 2)
#     print(li)
# printList()
# Task37:
# def printList():
#     li = list()
#     for i in range(1, 21):
#         li.append(i ** 2)
#     print(li[0:5])
# printList()
# Task38:
# def printList():
#     li = list()
#     for i in range(1, 21):
#         li.append(i ** 2)
#     print(li[-5:])
# printList()
# Task39:
# def printList():
#     li = list()
#     for i in range(1, 21):
#         li.append(i ** 2)
#     print(li[5:])
# printList()
# Task40:
# def printTuple():
#     li = list()
#     for i in range(1, 21):
#         li.append(i ** 2)
#     print(tuple(li))
# printTuple()
# Task41:
# tp=(1,2,3,4,5,6,7,8,9,10)
# tp1=tp[:5]
# tp2=tp[5:]
# print(tp1)
# print(tp2)
# Task42:
# tp=(1,2,3,4,5,6,7,8,9,10)
# li=list()
# for i in tp:
# 	if i%2==0:
# 		li.append(i)
# tp2=tuple(li)
# print(tp2)
# Task43:
# s=input("Enter the string:")
# if s=="yes" or s=="YES" or s=="Yes":
#     print("Yes")
# else:
#     print("No")
# Task44:
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = filter(lambda x: x%2==0, li)
# print(evenNumbers)
# Task45:
# li = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, li)
# print(squaredNumbers)
# Task46:
# li = [1,2,3,4,5,6,7,8,9,10]
# evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
# print(evenNumbers)
# Task47:
# evenNumbers = filter(lambda x: x%2==0, range(1,21))
# print(evenNumbers)
# Task48:
# squaredNumbers = map(lambda x: x**2, range(1,21))
# print(squaredNumbers)
# Task49:
# class American(object):
#     @staticmethod
#     def printNationality():
#         print("America")
# anAmerican = American()
# anAmerican.printNationality()
# American.printNationality()
# Task50:
# class American(object):
#     pass
# class NewYorker(American):
#     pass
# anAmerican = American()
# aNewYorker = NewYorker()
# print(anAmerican)
# print(aNewYorker)
# Task51:
# class Circle(object):
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return self.radius**2*3.14
# aCircle = Circle(5)
# print(aCircle.area())
# Task52:
# class Rectangle(object):
#     def __init__(self, l, w):
#         self.length = l
#         self.width = w
#     def area(self):
#         return self.length*self.width
# aRectangle = Rectangle(20,30)
# print(aRectangle.area())
# Task53:
# class Shape(object):
#     def __init__(self):
#         pass
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, l):
#         Shape.__init__(self)
#         self.length = l
#     def area(self):
#         return self.length*self.length
# aSquare= Square(9)
# print(aSquare.area())
# Task54:
# print("something wrong")
# raise RuntimeError('something wrong')
# Task55:
# def throws():
#     return 5/0
# try:
#     throws()
# except ZeroDivisionError:
#     print("division by zero!")
# except Exception:
#     print("Caught an exception")
# finally:
#     print("In finally block for cleanup")
# Task56:
# class MyError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
# error =MyError("something wrong")
# Task57:
# import re
# emailAddress =input("enter the email address:")
# pat2 = "(\w+)@((\w+\.)+(com))"
# r2 = re.match(pat2,emailAddress)
# print(r2.group(1))
# Task58:
# import re
# emailAddress =input("enter the email address:")
# pat2 = "(\w+)@(\w+)\.(com)"
# r2 = re.match(pat2,emailAddress)
# print(r2.group(2))
# Task59:
# import re
# s =input("enter input:")
# print(re.findall("\d+",s))
# Task60:
# unicodeString = u"hello world!"
# print(unicodeString)
# Task61:
# s =input("enter the input:")
# u =(s ,"utf-8")
# print(u)
# #Task62:
# # -*- coding: utf-8 -*-
# Task63:
# n=int(input("enter the input:"))
# sum=0.0
# for i in range(1,n+1):
#     sum += float(float(i)/(i+1))
# print(sum)
# Task64:
# def f(n):
#     if n==0:
#         return 0
#     else:
#         return f(n-1)+100
# n=int(input("enter the input:"))
# print(f(n))
# Task65:
# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
# n=int(input("enter the input:"))
# print(f(n))
# Task66:
# def f(n):
#     if n == 0: return 0
#     elif n == 1: return 1
#     else: return f(n-1)+f(n-2)
# n=int(input("Enter input:"))
# values = [str(f(x)) for x in range(0, n+1)]
# print(",".join(values))
# Task67:
# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1
# n=int(input("Enter a value:"))
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))
# print(",".join(values))
# Task68:
# def NumGenerator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# n=int(input("Eter the input:"))
# values = []
# for i in NumGenerator(n):
#     values.append(str(i))
# print(",".join(values))
# Task69:
# li = [2,4,6,8]
# for i in li:
#     assert i%2==0
# print("The even numbers list is",li)
# Task70:
# expression =input("Enter the input:")
# print(eval(expression))
# Task71:
# import math
# def bin_search(li, element):
#     bottom = 0
#     top = len(li)-1
#     index = -1
#     while top>=bottom and index==-1:
#         mid = int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index = mid
#         elif li[mid]>element:
#             top = mid-1
#         else:
#             bottom = mid+1
#     return index
# li=[2,5,7,9,11,17,222]
# print(bin_search(li,11))
# print(bin_search(li,12))
# Task72:
# import math
# def bin_search(li, element):
#     bottom = 0
#     top = len(li)-1
#     index = -1
#     while top>=bottom and index==-1:
#         mid = int(math.floor((top+bottom)/2.0))
#         if li[mid]==element:
#             index = mid
#         elif li[mid]>element:
#             top = mid-1
#         else:
#             bottom = mid+1
#     return index
# li=[1,3,4,2,7,9,33,44,78,95]
# print(bin_search(li,11))
# print(bin_search(li,12))
# Task73:
# import random
# print(random.random()*100)
# Task74:
# import random
# print(random.random()*100-5)
# Task75:
# import random
# print(random.choice([i for i in range(11) if i%2==0]))
# Task76:
# import random
# print(random.choice([i for i in range(100) if i%5==0 and i%7==0]))
# Task77:
# import random
# print(random.sample(range(100,201), 5))
# Task78:
# import random
# print(random.sample([i for i in range(100,201) if i%2==0], 5))
# Task79:
# import random
# print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
# Task80:
# import random
# print(random.randrange(7,16))
# Task81:
# import zlib
# str=b'hello world!hello world!hello world!hello world!'
# t = zlib.compress(str)
# print(t)
# print(zlib.decompress(t))
# Task82:
# from timeit import Timer
# t = Timer("for i in range(100):1+1")
# print(t.timeit())
# Task83:
# from random import shuffle
# li = [3,6,7,8]
# shuffle(li)
# print(li)
# Task84:
# subjects=["I", "You"]
# verbs=["Play", "Love"]
# objects=["Hockey","Football"]
# for i in range(len(subjects)):
#     for j in range(len(verbs)):
#         for k in range(len(objects)):
#             sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
#             print(sentence)
# Task85:
# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print(li)
# Task86:
# li = [12,24,35,70,88,120,155]
# li = [x for x in li if x%5!=0 and x%7!=0]
# print(li)
# Task87:
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i%2!=0]
# print(li)
# Task88:
# array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array)
# Task89:
# li = [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
# print(li)
# Task90:
# li = [12,24,35,24,88,120,155]
# li = [x for x in li if x!=24]
# print(li)
# Task91:
# set1=set([1,3,6,78,35,55])
# set2=set([12,24,35,24,88,120,155])
# set1=set1&set2
# li=list(set1)
# print (li)
# Task92:
# def removeDuplicate( li ):
#     newli=[]
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add( item )
#             newli.append(item)
#     return newli
# li=[12,24,35,24,88,120,155,88,120,155]
# print(removeDuplicate(li))
# Task93:
# class Person(object):
#     def getGender( self ):
#         return "Unknown"
# class Male( Person ):
#     def getGender( self ):
#         return "Male"
# class Female( Person ):
#     def getGender( self ):
#         return "Female"
# aMale = Male()
# aFemale= Female()
# print(aMale.getGender())
# print(aFemale.getGender())
# Task94:
# dic = {}
# s=input("Enter the string:")
# for s in s:
#     dic[s] = dic.get(s,0)+1
# print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
# Task95:
# s=input("enter the string:")
# s = s[::-1]
# print(s)
# Task96:
# s=input("Enter the string:")
# s = s[::2]
# print(s)
# Task97:
# import itertools
# print(list(itertools.permutations([1,2,3])))
# Task98:
# def solve(numheads,numlegs):
#     ns='No solutions!'
#     for i in range(numheads+1):
#         j=numheads-i
#         if 2*i+4*j==numlegs:
#             return i,j
#     return ns,ns
# numheads=35
# numlegs=94
# solutions=solve(numheads,numlegs)
# print(solutions)
