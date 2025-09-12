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

num = int(input("Enter a number:"))

# while num !=0:
#   dig = num % 10
#   print(dig,end='')
#   num = num //10
  
li = []
while num % 10 !=0:
  dig = num % 10
  li.append(dig)
  num = num //10

print(li)
str =""
str.join(li)
print(str)
