# print("Control flow")

# email = input("Enter your email:")
# password = input("Enter your password:")

# if email =="abc@gmail.com" and password == "1234":
#   print("login successful")
# elif email == "abc@gmail.com" and password != "1234":
#   print("Incorrect password")
#   password = input("Enter password again:")
#   if password =="1234":
#     print("Welcpme finally")
#   else:
#     print("Tumse nahi ho payega")
# else:
#   print("Login failed")

# age = 25
# if age<=12:
#   print("Child")
# elif age <=19:
#   print("Teenger")
# elif age <=24:
#   print("Young Adult")
# else:
#   print("Adult")

#max of three numbers
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# num3 = int(input("Enter a number:"))
# if num1 >num2 and num1 > num3:
#   print(num1," is greatest")
# elif num2>num3:
#   print(num2," is greatest")
# else:
#   print(num3," is greatest")

#match case
# num1 = float(input("Enter a number:"))
# num2 = float(input("Enter a number:"))
# op = input("Enter an operator:")
# match op:
#   case '+':
#     print(num1+num2)
#   case '-':
#     print(num1 -num2)
#   case '*':
#     print(num1*num2)
#   case '/':
#     print(num1/num2)
#   case _:
#     print("Operation not valid")
  
#session 3 tasks
# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%
# ctc = int(input("Enter ctc in lakhs:"))
# hra = ctc * 0.1
# da = ctc * 0.05
# pf = ctc * 0.03
# salary = ctc - (hra + da + pf)
# if salary < 5:
#   tax = salary * 0.0
#   monthly_salary = (salary - tax)/12
# elif salary >=5 and salary <10:
#   tax = salary * 0.1
#   monthly_salary = (salary - tax)/12
# elif salary >=10 and salary <20:
#   tax = salary * 0.2
#   monthly_salary = (salary - tax)/12
# else:
#   tax = salary * 0.3
#   monthly_salary = (salary - tax)/12
  
# print("monthly salary:",monthly_salary*100000)

# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

angle1 = float(input("Enter an angle:"))
angle2 = float(input("Enter an angle:"))
angle3 = float(input("Enter an angle:"))

sum = angle1+angle2+angle3

