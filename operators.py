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


#relational operator - to compare between two things
# print(4>5) #false
# print(10<34) #true
# print(4>=4) #true
# print(5<=4) #false
# print(4 == 4) #true
# print(10 !=30) #true

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
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))

if num1 < num3 and num1 < num2:
  print(f"{num1} is the min")
elif num2 < num1 and num2 < num3:
  print(f"{num2} is the min")
else:
  print(f"{num3} is the min")
  






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
