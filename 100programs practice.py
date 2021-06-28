#Task1:
# l=[]
# for i in range(2000,3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(i)
# print(l)
#output:[2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114,
# 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233,
# 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366,
# 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499,
# 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632,
# 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758,
# 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891,
# 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024,
# 3031, 3038,3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157,
# 3164, 3171, 3178, 3192, 3199]

#Task2:
#Method:1
# n=int(input("enter the value:"))
# fact=1
# for i in range(1,n+1):               #using for loop
#     fact=fact*i
# print(fact)
#Method:2
# n=int(input("enter the number:"))
# i=1
# fact=1
# while i<=n:                #using whileloop
#     fact=fact*i
#     i=i+1
# print(fact)
#Method:3
# def fact(n):
#     fact = 1
#     for i in range(1,n+1):   #using functions
#         fact=fact*i
#     print(fact)
# fact(5)
#output:
# enter the number:5
# 120

#Task3:
# n=int(input("Enter the value:"))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)
# output:
# Enter the value:8
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#Task4:
# li=input("enter the values:")
# l=li.split(',')
# tuple=tuple(l)
# list=list(l)
# print(tuple)
# print(list)
# output:
# enter the values:32,54,65,76
# ('32', '54', '65', '76')
# ['32', '54', '65', '76']
#Task5:
# class  InputOutString(object):
#     def __int__(self):
#         self.s=""
#     def getString(self):
#         self.s=input("Enter the string:")
#     def printString(self):
#         print(self.s.upper())
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
# output:
# Enter the string:bhargavi
# BHARGAVI
#Task6:
# import math
# c=50
# h=30
# value =[]
# items=[x for x in input("enter the values:").split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
# print(','.join(value))
# output:
# enter the values:100,150,180
#18,22,24
#Task7:
# input_str =input('Enter the data:')
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col
# print(multilist)
# output:
# Enter the data:3,4
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
#Task8:
# items=[x for x in input("enter the strings:").split(',')]
# items.sort()
# print(','.join(items))
# output:
# enter the strings:ball,apple,dog,eagle
# apple,ball,dog,eagle
#Task9:
# lines = []
# while True:
#      s = input()
#      if s:
#          lines.append(s.upper())
#      else:
#          break;
# for sentence in lines:
#      print(sentence)
# output:
# hello world
# practice makes perfect
# HELLO WORLD
# PRACTICE MAKES PERFECT
#Task10:
# n=input("Enter the sentence:")
# words=[word for word in n.split(" ")]
# print(" ".join(sorted(list(set(words)))))
# output:
# Enter the sentence:
# hello world and practice makes perfect and hello world again
# again and hello makes perfect practice world
