#question 1
# ctc = int(input("Enter CTC:"))
# hra = ctc * 0.1
# da = ctc * 0.05
# pf = ctc * 0.03

# salary = ctc - (hra + da + pf)


# if salary < 5:
#   tax = ctc * 0.0
#   salary = (salary - tax)/12
# elif salary >=5 and salary < 10:
#   tax = ctc * 0.1
#   salary = (salary - tax)/12
# elif salary >=10 and salary<20:
#   tax = ctc * 0.2
#   salary = (salary - tax)/12
# else:
#   tax = ctc * 0.3
#   salary = (salary - tax)/12
  
# print(salary * 100000)

#question 2
# angle1 = float(input("Enter a angle:"))
# angle2 = float(input("Enter a angle:"))
# angle3 = float(input("Enter a angle:"))

# sum_of_angles = angle1 + angle2 + angle3

# if sum_of_angles ==180.0 and (angle1 >0 and angle2 >0 and angle3 >0) :
#   print("Can form a triangle")
# else:
#   print("Cannot form a triangle")

#question 3
# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

# cost_price = int(input("Enter cost price:"))
# selling_price = int(input("Enter selling price:"))

# if selling_price > cost_price:
#   print("Profit")
# elif selling_price == cost_price:
#   print("No profit or loss")
# else:
#   print("Loss")

# # Problem 6 - Find the factorial of a given number.
# num = int(input("Enter a number:"))
# fact = 1
# if num < 0 :
#   print("Factorial doesn't exist for negative")
# elif num ==0:
#   print("The factorial is 1")
# else:
#   for i in range(1,num+1):
#     fact *= i
#   print(fact)

# num = int(input("Enter a number:"))

# # while num !=0:
# #   dig = num % 10
# #   print(dig,end='')
# #   num = num //10
  
# li = []
# while num % 10 !=0:
#   dig = num % 10
#   li.append(dig)
#   num = num //10

# print(li)
# str =""
# str.join(li)
# print(str)


# a = int(input("a = "))
# b = int(input("b = "))
# operator = int(input("operator = "))
# if operator == 1:
#   print(a+b)
# elif operator ==2:
#   print(a-b)
# elif operator ==3:
#   print(a*b)
# else:
#   print("Invalid Input")

#temperature check
# current_temp = float(input("Enter current temp:"))
# if current_temp <20:
#   print("It's cold")
# elif current_temp>=20 and current_temp<=30:
#   print("It's pleasant")
# else:
#   print("It's hot")
  
#login system
# username = input("Enter username:")
# password = input("Enter password:")
# if username =="admin" and password == "1234":
#   print("Login Successful")
# else:
#   print("Access denied")
  
#evenodd
# num = int(input("Enter a number:"))
# if num % 2 ==0:
#   print("Even")
# else:
#   print("Odd")
                    
#problem no -4 
# user_input = input("""
#     Hi.What do you want?
#     1.cm to fit
#     2.km to miles
#     3.USD to BDT
#     4.exit
#   """)
# if user_input == "1":
#   cm = float(input("Enter cm value:"))
#   feet = cm/30.48
#   print(f"{cm} cm is {feet} feet")
# elif user_input =="2":
#   km = float(input("Enter km value:"))
#   miles = km * 0.6214
#   print(f"{km} kilo is {miles} miles")
# elif user_input =="3":
#   usd = float(input("Enter USD:"))
#   bdt = usd * 122.53
#   print(f"{usd} usd is {bdt} bdt")
# else:
#   print("Exited")
  
#fibonacci series upto 10 terms
                    
#movie ticket pricing
# age = int(input("Enter your age:"))

# if age<18:
#   if age<12:
#     print("Ticket is 100")
#   elif age >=12:
#     print("Ticket is 150")
# else:
#   print("Ticket is 200")
  
#number comparison
# num1 = int(input("Enter a number"))
# num2 = int(input("Enter a number"))
# num3 = int(input("Enter a number"))
# if num1 == num2 or num1 ==num2
# if num1 > num2 and num1 > num3:
#   print(num1," is the greatest")
# elif num2 > num3:
#   print(num2, " is the greatest")
# el:
#   print(num3, " is the greatest")
# else:
#   print("They are equal")

#fibonacci 
# ini = 0 
# mid = 1 
# # fin = mid + ini
# print(ini,mid,sep=',')
# for i in range(2,10):
#   fin = mid + ini
#   print(fin)
#   ini = mid
#   mid = fin 
  
#factorial of a given number 
# i = 1
# fact = 1
# num = int(input("Enter a number:"))
# for i in range(num,0,-1):
#   fact *= num
#   num = num-1
# print(fact)

# num = 7864
# li = []
# while num !=0:
#   dig = num % 10
#   num = num // 10
#   li.append(dig)
  
#guessing a number
# import random
# counter = 0
# rand_num = random.randint(1,10)
# while True:
#   counter+=1
#   user_input = int(input("Guess a number:"))
#   if user_input == rand_num:
#     print("You guessed right")
#     print(f"Guess at {counter} attempt")
#     break
#   elif user_input > rand_num:
#     print("You guessed higher")
#   elif user_input< rand_num:
#     print("You guessed lower")
  
    # user_input = int(input("Guess again"))

#list filtering
# numbers = [12,23,21,33,22,33,44,24,142,1,1,414,42,4,42]
# for i in range(len(numbers)):
#   if numbers[i]%2==0:
#     print(numbers[i])
#   else:
#     continue

#login with attempts

loop_count =1
while loop_count<=3:
  username = input("Enter username:")
  password = input("Enter password:")
  if username == "user" and password=="pass123":
    print("Login successful")
    break
  else:
    username = input("You have 2 chances:")
    
    
