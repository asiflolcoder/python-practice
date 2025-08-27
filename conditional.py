age = 16
if age>18:
  print("Eligible to vote")
else:
  print("Not eligible to vote")

#elif statement
age = 34
if age <=10:
  print("Child")
elif age <=18:
  print("Teenager")
elif age <=25:
  print("Young Adult")
else:
  print("Adult")
  
#nested if else
num = -4
if num>0:
  if num%2==0:
    print("Even")
  else:
    print("Odd")
else:
  if num==0:
    print("Zero")
  else:
    print("Negative")
    
#calcutor match program

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))
# op = input("Enter an operator:")
# match op:
#   case "+":
#     print(num1+num2)
#   case "-":
#     print(num1-num2)
#   case "*":
#     print(num1*num2)
#   case "/":
#     print(num1/num2)
#   case _ :
#     print("Operation invalid")
  
age = 10
member = True
if age > 18:
  if member:
    print("Ticket price in $12")
  else:
    print("Ticket price in $20")
else:
  if member:
    print("Ticket price is $8")
  else:
    print("Ticket price is $10")
    
#if else in one line

# x = 10
# y = 5
# res = "x is greater" if x > y else "y is greater"
# print(res)

# budget = 60
# price = 9.99
# if budget >= 50 and price <=10:
#   print("Buy 3 pieces")
# if budget >=100 and price <=20:
#   print("Buy two pieces")

# print("Asif" and 99)
# print("Asif" or 99)

#problem 1
# j_angry = True
# s_angry = True
# if j_angry and s_angry:
#   print("True")
# else:
#   print("False")
  
# if x % 2 ==0:
#   return "Even"
# else:
#   return "Odd"


# if "cat" in str:
#   print("True")
# else:
#   print("False")c
str = "bazingaa"

# cat_num = 0
# hat_num = 0

# if "cat" in str:
#   cat_num+=1
# if "hat" in str:
#   hat_num=+1

# if cat_num == hat_num:
#   print("True")
# else:
#   print("False")

def bigNumber(a):
  if a >100:
    print("Big")
  else:
    print("Number")
  
a = int(input())
bigNumber(a)