
# -*- coding: utf-8 -*-

# Q-1: Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.


# class Rectangle:
#   def __init__(self,length,width):
#     self.length = length
#     self.width = width
    
#   def perimeter(self):
#     parameter = 2 * (self.length + self.width)
#     return parameter
  
#   def area(self):
#     area = self.length * self.width
#     return area
  
#   def display(self):
#     print("The length of rectangle is:",self.length)
#     print("The width of rectangle is:",self.width)
#     print("The perimeter of rectangle is:",self.perimeter())
#     print("The area of rectangle is:",self.area())
  
# my_rectangle = Rectangle(3,4)
# my_rectangle.display()

# class BankAccount:
#   def __init__(self,accountNumber,name,balance):
#     self.accountNumber = accountNumber
#     self.name = name
#     self.balance = balance
    
#   def Deposit(self,deposit):
#     if deposit<=0:
#       print("Deposit must be positive")
#     else:
#       self.balance = self.balance + deposit
#     return self.balance
    
#   def Withdrawal(self,withdraw):
#     self.balance = self.balance - withdraw
#     return self.balance
  
#   def bankFees(self):
#     fees = self.balance * (5/100)
#     self.balance = self.balance - fees
  
#   def get_balance(self):
#     return f"{self.balance} ₹"
      
#   def display(self):
#     print("Account number : ",self.accountNumber)
#     print("Account Name : ",self.name)
#     # print(f"Account Balance :\u20B9 self.balance)
    

# newAccount = BankAccount(2178514584,"Mandy",2800)
# newAccount.Withdrawal(700)
# newAccount.Deposit(1000)
# newAccount.display()

#q-3

# class Computation:
#   def __init__(self):
#     pass
  
#   def Factorial(self,n):
#     for i in range(1,n+1):
#       fact = 1
#       fact*=i
#     return f"The factorial of {n} is : {fact}"
#     # return 'The factorial of {} is : {}'.format(n,fact)
    
#   def naturalSum(self,n):
#     sum = (n * (n+1))/2
#     return f"The sum of {n} number is {sum}"
  
  
    
# num = Computation()
# print(num.Factorial(6))
# print(num.naturalSum(20))


# Q-4
# import random

# class FlashCard:
#   def __init__(self,name,color):
#     self.fruit ={}
#     # self.fruit[name]= color
#     # print(self.fruit)
    
#   def add_fruit(self,)
    
  # def get_keys(self):
  #   count = 0 
  #   for i in self.frui
    
  # def get_fruit(self):
  #   random_key = random.randint(1,)
  
# fruit = FlashCard("Banana","yellow")


#Q-5
