print("Operators in python")

#operators - symbols to carry out calculations
# a(operand) +(operator) b(operand)

# a = 100
# b = 50
# sum = a + b #150
# sub = a - b #50
# multi = a * b #5000
# div = a / b #2.0
# exp = a ** b #large number
# floor_div = a // b #2
# mod = a % b #0

# print(sum)
# print(sub)
# print(multi)
# print(div)
# print(exp)
# print(floor_div)
# print(mod)
#operator precedence-(),**,/ * % //,+-
print(20 + (3*4) - 2 *4 /4)
# print(2**3**2)

#relational operator - to compare between two things
# print(4>5) #false
# print(10<34) #true
# print(4>=4) #true
# print(5<=4) #false
# print(4 == 4) #true
# print(10 !=30) #true
# print(2 == 2.00)


#logical -and,or,not
# print(12 and "Asif")
# print("" and 200)

# print(12 or 13 or 23)
# print("" or 20 or 23)

# print(not 12)

#bitwise operator - bit by bit kaj kore
# print( 10 & 4)
# print(5 & 5)
# print(10 ^ 5)
# print(~4)

#assignment operator- =+,=-,*=,/=
# a = 10
# b = 5
# a+=b
# print(a)
# a-=b
# print(a)
# a*=b
# print(a)

# a /=b
# print(a)
# a %=b
# print(a)
# # a++
# ++a
# print(a)
# print(a)

#membership operator-in,not in
l = [1,2,3,4]
str1 = "Hello World"
t = ("Asif",25,True)

# print(1 in l)
# print(10 not in l)
# print("A" in str1)
# print("o" not in str1)
# print(25 in t)
# print(False not in t)

# num = int(input("Enter a number:"))
# dig1 = num % 10
# num = num //10
# dig2 = num % 10
# num = num //10
# dig3 = num %10
# num = num //10
# dig4 = num % 10
# print(dig1+dig2+dig3+dig4)

#identity operator- is,is not
# print(12 is 12)
# print(12 is not 12)

#if else in python
#login process 
# email = input("Enter you email:")
# password = input("Enter password:")

# if email =="asif@gmail.com" and password =="1234":
#   print("login successful")
# elif email == "asif@gmail.com" and password !="1234":
#   print("Wrong password")
#   password = input("Enter password:")
#   if password =="1234":
#     print("Login success")
# else:
#   print("Wrong info")

#find the min of 3 given numbers
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# num3 = int(input("Enter a number:"))

# if num1 < num3 and num1 < num2:
#   print(f"{num1} is the min")
# elif num2 < num1 and num2 < num3:
#   print(f"{num2} is the min")
# else:
#   print(f"{num3} is the min")
  
#match case statement
# x = "monday"
# match x:
#   case "Sunday":
#     print("Today is sunday")
#   case "Monday":
#     print("Today is monday")
#   case "Tuesday":
#     print("Today is tuesday")
#   case _:
#     print("Invalid day")



#operator tasks
# ctc = int(input("Enter ctc:"))
# hra = ctc * 0.1
# da = ctc * 0.05
# pf = ctc * 0.03
# salary = ctc - (hra + da + pf) 
# if ctc<5:
#   salary = salary
# elif ctc >=5 and ctc < 10:
#   tax = ctc*0.1
#   salary = salary - tax
# elif ctc >=10 and ctc <20:
#   tax = ctc *0.2
#   salary = salary - tax
# elif ctc >=20:
#   tax = ctc * 0.3
#   salary = salary - tax

#problem - 2
# angle1 = float(input("enter a angle:"))
# angle2 = float(input("enter a angle:"))
# angle3 = float(input("enter a angle:"))

# if (angle1+angle2) > angle3 or (angle2 + angle3) >angle1 or (angle3+angle1) >angle2:
#   print("Can be a triangle")
# else:
#   print("Cannot form a triangle")
  
# sum_of_angles = angle1 + angle2 + angle3
# if sum_of_angles == 180 and (angle1>0 and angle2>0 and angle3>0):
#   print("Can be a triangle")
# else:
#   print("Can't be a triangle")
  
# cost = float(input("Enter cost price:"))
# sell = float(input("Enter selling price:"))

# if cost > sell:
#   print("Loss")
# elif cost < sell:
#   print("Profit")
# else:
#   print("Even")

#problem 4 - menu driven program
# while True:
#   user_input = input("""
#   1.cm to ft
#   2.km to miles
#   3.USD to BDT
#   4.exit\n""")

#   if user_input == '1':
#     cm = float(input("Enter cm value:"))
#     fit = cm /30.48
#     print(f"{cm} cm = {fit} ft")
#   elif user_input =="2":
#     km = float(input("Enter km value:"))
#     miles = km /1.61
#     print(f"{km} km = {miles} miles")
#   elif user_input == "3":
#     usd = float(input("Enter usd:"))
#     bdt = usd * 122.27
#     print(f"{usd} usd = {bdt} bdt")
#   else:
#     print("Exited")
#     break
                  
#problem 5 - fibonacci sequence
# ini = 0 
# mid = 1
# for i in range(1,10):
  

#problem 6
# n = int(input("Enter a number:")) 
# fact = 1
# for i in range(1,n+1):
#   fact *= i

# print(f"factorial of {n} is : {fact}")

#problem 7 
# n = 76542
# s =""
# while n % 10 != 0:
#   dig = n % 10
#   s +=dig
#   n = n // 10
# print(s)

#problem 8 
# N = int(input())
# sum = 0
# i = 0
# while i < N :
#   if i % 5 == 0:
#     continue
#   else:
#     sum += i
  
#   i +=1



#control flow 
#operators
# exp1 = 34.5 + 45
# #arithmetic(+,-,*,/,%,//,**)
# add = 234.5 + 45
# sub = 23 - 45.0
# multi = 34 * 45.0
# div = 45 / 4
# mod = 34 % 5
# flo_div = 23 // 10
# print(add,sub,multi,div,mod,flo_div)
#precedence - (), **,* / // %,+ -
#relational operator - ><>=<=.==,!=
# print(45 > 33)
# print(34 < 23)
# print(34>=45)
# print(44<=23)
# print(12 == 12)
# print(12 is 23)
# print(12.0 == 12)
# l1 = [12,3,4]
# l2 = [12,3,4]
# print(l1 is l2)
# print(l1 == l2)
s1 = "Asif"
s2 = "Asif"
# print(s1 == s2)
# print(s1 is s2)
t1 =(1,2,3)
t2 =(1,2,3)
# print(t1 == t2)
# print(t1 is t2)
#assignment - +=,-=
# a = 30
# a+=30
# print(a)
# a-=40
# print(a)
# a*=30
# print(a)
# a /= 15
# print(a)
# a %= 3
# print(a)
#logical operator - and,or,not
# print(true and true)
# print("Asif" and "23")
# print("" and 23)

# print(23 or 12)
# print("" or "Asif")

#membership operator-in,not in
# print(4 in [1,2,3])
# print(5 not in (1,234))
#if else

#palindrome number
# num = int(input("Enter a number:"))
# num_str = str(num)
# num_rev = num_str[::-1]
# if num_str == num_rev:
#   print("Palindrome")
# else:
#   print("Not palindrome")
  

#sum of digits
# num = int(input("Enter a number:"))
# sum = 0
# while num % 10 !=0:
#   dig = num % 10
#   sum += dig
#   num = num // 10
# print(sum)

#count even and odd digits
# num = int(input("Enter a number:"))
# even = 0
# odd = 0
# while num % 10 !=0:
#   dig = num % 10
#   if dig % 2 ==0:
#     even += 1
#   else:
#     odd += 1
#   num = num // 10
# print("Even digits:{}".format(even))
# print("Odd digits:{}".format(odd))

#largest of 3 numbers
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# num3 = int(input("Enter a number:"))
# if num1 > num2 and num1 > num3:
#   print(f"{num1} is the largest")
# elif num2 > num3:
#   print(f"{num2} is the largest")
# else:
#   print(f"{num3} is the largest")

#electricity bill calculator
# units = float(input("Enter units:"))
# bill = 0
# if units >=0 and units<=100:
#   price = 5
#   bill_under_100 = units * 5
  
# if units >=101 and units <= 200:
#   price = 7
#   bill_under_200 = bill_under_100 + 

#multiplication table of n
n = int(input("Enter :"))

