print("Operators and control flow")

#arithmetic(+,-,*,/,//,%,**)
# num1 = 24
# num2 = 11
# add = num1 + num2
# sub = num1 - num2
# multi = num1 * num2
# div = num1 / num2
# int_div = num1 //num2
# mod = num1 %num2
# print(add)
# print(sub)
# print(multi)
# print(div)
# print(int_div)
# print(mod)

# a ,b = 3,4
# print(a**b)

#precedence of arithmetic operator-(),**(RL) // % /*,+,-
# a = 3 ** 4 ** 3
# # print(a)
# b = (3+4)*4 +4-3*3
# print(b)

#comparison operator - (>,>=,<,<=,==,!=)-returns boolean
# print(4>5)
# print(23<45)
# print(55>=55)
# print(44<=23)
# print(44==34)
# print(34!=34)

#is vs ==
# print(12==23)
# print(12 is 12)

# l1 = [1,2,3]
# l2 = [1,2,3]
# print(l1 == l2)
# print(l1 is l2)

#logical operator
# print(True and False)
# print(True and True)
# print(False and True)
# print(False and False)
# print(12 and "Asif")
# print(0 and "Probin")
# print(False and [1,2,3])

# print(True or False)
# print(True or True)
# print(False or True)
# print(False or False)
# print("Asif" or 12)
# print(0 or "Asif")

# print(23 and "Asif") #Asif
# print(0 or 2) # 2
# print(0 and True) # 0
# print("Asif" or False) #Asif

# print(not 23)
# print(not False)

#bitwise operator - performs on bits

#operators-symbols that perform calculations
# num1 = 20
# num2 = 30
# a = num1 + num2
# #arithmetic operator - (+,-,*,/,%,//,**)
# sum = num1 + num2
# print(sum)
# sub = num1 - num2
# print(sub)
# multi = num1 * num2
# print(multi)
# div = num1 / num2
# print(div)
# flo = num2 //num1
# print(flo)
# mod = num2 % num1 
# print(mod)

# a,b = 4,5
# print(a**b)

#precedence of arithmetic operator-(),% // **,/ * + -
# a,b,c = 2,3,4
# # print(a**b**c)
# x = 3 + 4 *(4+3)/4 -4
# print(x)

#relational / comparison operator - >,>=,<,<=,==,!=
# print(3>4) #false
# print(34>=31) #true
# print(10<42) #true
# print(98<=43) #false
# print(3==4) #false
# print(4!=4) #false

#logical operator - and,or,not
# print(True and True)
# print(False and True)
# print(True and False)
# print(False and False)
# print("Asif" and 23)
# print("" and "Asif")

# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)
# print("Asif" or 23)
# print("" or "Asif")

# print(not "Asif")
# print(not "")
# print(not False)
# print(not None)

# print("Hello" or "Python") #"Hello"
# print("" and "") #""
# print("Asif" and "") #""
# print(None or "Js") #js

#bitwise operator
# print(3 & 4)


#asignment operator - +=,-=,*=,/=,%=,
# x = 100
# print(x)
# x+=10
# print(x)
# x-=20
# print(x)
# x*=20
# print(x)
# x/=35
# print(x)
# x %= 10
# print(x)

#membership operator - not in ,in(sequence data type based)
# print(2 in [2,3,4])
# print(34 in [23,43,22])
# print(43 not in [23,43,12])
# print(4 in (3,3,2,4))
# print(5 in (2,3,2,1))
# print(1 not in (3,4,3,2))
# print(1 not in (1,1,1))

#sum of a 4 digit number
# num = int(input("Enter a 4 digit number:"))
# d1 = num % 10
# num = num //10
# d2 = num %10
# num = num //10
# d3 = num % 10
# num = num //10
# d4 = num %10
# num = num //10
# sum = d1 + d2 + d3 + d4
# print("Sum of 4 digits:",sum)

#if-elseif-else
# age = 15
# if age>=18:
#   print("He can vote")
# else:
#   print("He cannot vote")
# marks = 56
# if marks >=90:
#   print("A+")
# elif marks >=80:
#   print("A")
# elif marks >=70:
#   print("B")
# elif marks >=60:
#   print("C")
# elif marks >=50:
#   print("D")
# else:
#   print("F")

#if esle - login program
# email = input("Enter email here:")
# password = input("Enter password:")
# if email =="asif@gmail.com" and password=="1234":
#   print("Welcome")
# elif email =="asif@gmail.com" and password !="1234":
#   print("Incorrect Password")
#   password = input("Enter password:")
#   if password=="1234":
#     print("Welcome")
#   else:
#     print("Beta tumse ho na payega")
# else:
#   print("Wrong Password")

#min of 3 numbers
# num1 = 11
# num2 = 15
# num3 = 21
# if num1 < num2 and num2 <num3:
#   print(num1," is min")
# elif num2 < num3 :
#   print(num2," is min")
# else:
#   print(num3," is min")
  
#menu driven program
# menu = input('''
#              Hi
#              How can i help you?
#              1.Enter 1 to create pin
#              2.Enter 2 to change pin
#              3.Enter 3 to check balance
#              4.Enter 4 to withdraw balnce
#              5.Enter 5 to go back to menu
#              ''')
# if menu =="1":
#   print("Enter pin")
# elif menu =="2":
#   print("Change pin")
# elif menu =="3":
#   print("Check Balance")
# elif menu =="4":
#   print("Withdraw balance")
# elif menu =="5":
#   print("Go to menu")

# import math 
# factorial = math.factorial(5)
# print(factorial)

# floor = math.floor(34.543)
# print(floor)

# remainder = math.remainder(10,3)
# print(remainder)

# sqrt = math.sqrt(16)
# print(sqrt)

# help('modules')

# import keyword
# print(keyword.kwlist)

# import random
# random_number = random.randint(1,100)
# print(random_number)

# random_choice = random.choice(['Asif','Emon','Hasan','Probin'])
# print(random_choice)

# shuffle = random.shuffle([1,2,3,4,5,6])
# print(shuffle)

import datetime
date = datetime.date(1996,12,11)
print(date)
# print(datetime)
# today = date.today()
# print(today)

# now = datetime.datetime.now()
# print(now)

# today = datetime.date.today()
# print(today)

# print(dir(datetime))

#loops - for ,while,
# l1 = [1,2,3,4,5]
# for x in l1:
#   print(x)
  
# t = (2,3,4,5,6)
# for x in t:
#   print(x)
  
# s = "Asif"
# for x in s:
#   print(x)

# for i in range(1,100,3):
#   print(i)
  
# for i in range(100,0,-1):
#   print(i)

# for i in range(0,11):
#   if i == 3:
#     break
#   print(i)

# for i in 'geeksforgeeks':
#   if i == 'e' or i == 's':
#     continue
#   print(i)
  
# for i in 'geeksforgeeks':
#   if i =='e' or i =='s':
#     break
#   print(i)

#for else with else 
# for i in "Asif":
#   if i == "A" or i =="f":
#     print("Hi")
# else:
#   print("Ho")

#nested for loops
# for i in range(1,5):
#   print(f"Iteration for {i}")
#   for j in range(1,5):
#     print(f"Iteration no {i} at {j}")
      
#multiplication table for 5
# for i in range(4,5):
#   for j in range(1,11):
#     multi = i * j
#     print(f"{i} * {j} = {multi}")

# l1 =[12,32,23,11,33,22,43]
# for i in range(len(l1)):
#   print(l1[i])

#while loops
# counter = 0
# while counter <=5:
#   print(counter)
#   counter+=1

# s1 = "geeksforgeeks"
# i = 0 
# for i in range(len(s1)):
#   if s1[i] == "e" or s1[i] =="s":
#     continue
#   print(s1[i])
  
# s1 = "geeksforgeeks"
# i = 0
# while i <len(s1):
#   if s1[i] == "e" or s1[i] =="s":
#     break
#   print(s1[i])
#   i +=1
  
# def multiplicationTable(N):
#     #code here 
#     for i in range(N,N+1):
#         for j in range(1,11):
#             multi = N * j
#             print(multi,end=' ')

# multiplicationTable(6)
  