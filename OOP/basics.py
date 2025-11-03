print("OOP Basics")

# l = [12,34,21,11]
# l.upper()
# l = [1,2,3,4,5]
# # l.upper()
# # s ="Hello"
# # s.append("a")
# print(type(l))

#create a class
# class Student:
#   pass

# asif = Student()

# class Student:
#   def __init__(self):
#     self.name = "Md Asif"
#     self.age = 24
#     print(f"{self.name} : {self.age}")
# student1 = Student()
# print(student1)

# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#     print(f"{self.name}:{self.age}")
    
# student1 = Student("Emon",25)
# student2 = Student("Probin",24)
    

# class Atm:
#   def __init__(self):
#     pass

# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age =age
#     # print(id(self))
#     print(f"My name is {self.name} and I am {self.age} years old")

# asif = Student("Asif",24)
# # print(id(asif))
# emon = Student("Emon",25)

# class Atm:
#   def __init__(self):
#     self.pin = ""
#     self.balance = 0
#     # print("Atm object created")
#     self.menu()
  
#   def menu(self):
#     user_input = input("""
#         Hi How can i help you?
#         1.create pin
#         2.change pin 
#         3.check balance
#         4.withdraw balance
#         5.Exit\n""")
    
#     if user_input =='1':
#       self.create_pin()
#     elif user_input =='2':
#       self.change_pin()
#     elif user_input == '3':
#       self.check_balance()
#     elif user_input =='4':
#       self.withdraw_balance()
#     else:
#       self.exit()
    
    
#   def create_pin(self):
#     user_pin = input("Enter your pin:")
#     self.pin = user_pin

#     user_balance = int(input("Enter your balance:"))
#     self.balance = user_balance
#     print("Pin created successfully")
#     self.menu()
      
      
#   def change_pin(self):
#     old_pin = input("Enter your pin:")
#     if old_pin == self.pin:
#       new_pin = input("Enter new pin:")
#       self.pin = new_pin
#       print("Pin changed successfully")
#     else:
#       print("Password wrong,can't change")
#     self.menu()
      
    
#   def check_balance(self):
#     pin = input("Enter your pin:")
#     if pin == self.pin:
#       print(f"You balance is {self.balance}")
#     else:
#       print("Wrong pin entered")
#     self.menu()
  
#   def withdraw_balance(self):
#     user_pin = input("Enter your piin:")
#     if self.pin == user_pin:
#       amount = int(input("Enter amount to withdraw:"))
#       if amount<=self.balance:
#         self.balance = self.balance - amount
#         print("Withdraw successful .New Balance:",self.balance)
#       else:
#         print("You don't have that much money")
#     else:
#       print("Wrong Pin entered")
#     self.menu()
    
#     def exit(self):
#       self.menu()      
      
  
# obj =Atm()

#adding two objects
# class Point:
#   def __init__(self,x,y):
#     self.x = x 
#     self.y = y
  
#   def __add__(self,other):
#     return (self.x +other.x,self.y+other.y)
  
# p1 = Point(2,4)
# p2 = Point(4,5)
# print(p1 + p2) 
  
# class Student:
#   def __init__(x):
#     print("Object created")
#     print(id(x))
    
# stu1 = Student()
# print(id(stu1))

#creating a customized data type - fraction
# class Fraction:
#   def __init__(self,x,y):
#     self.x = x
#     self.y = y
  
#   def __str__(self):
#     return '{}/{}'.format(self.x,self.y)
  
#   def __add__(self,other):
#     num = self.x * other.y + self.y * other.x
#     den = self.y * other.y
#     return '{}/{}'.format(num,den)
  
#   def __sub__(self,other):
#     self.num = self.x * other.y - self.y * other.x
#     self.den = self.y * other.y
#     return '{}/{}'.format(self.num,self.den)
  
#   def __mul__(self,other):
#     self.num = self.x * other.x
#     self.den = self.y * other.y
#     return '{}/{}'.format(self.num,self.den)
  
#   def __truediv__(self,other):
#     self.num = self.x * other.y 
#     self.den = self.y * other.x
#     return '{}/{}'.format(self.num,self.den)
  
  
# obj1 = Fraction(3,4)
# obj2 = Fraction(4,5)
# print(obj1+obj2)
# print(obj1 - obj2)
# print(obj1 * obj2)
# print(obj1 / obj2)
# # print(obj1)

# class Rectangle:
#   def __init__(self,length,width):
#     self.length = length
#     self.width = width
    
#   def perimeter(self):
#     perimeter = 2 * (self.length + self.width)
#     return perimeter
    
#   def area(self):
#     area = self.length * self.width
#     return area
  
#   def display(self):
#     print(f"The length of rectangle is: {self.length}")
#     print(f"The width of rectangle is: {self.width}")
#     print(f"The perimeter of rectangle is: {self.perimeter()}")
#     print(f"The area of rectangle is: {self.area()}")
    
# my_rectangle = Rectangle(3,4)
# my_rectangle.display()

# class BankAccount:
#   def __init__(self,accountNumber,name,balance):
#     self.acc_num = accountNumber
#     self.name = name
#     self.balance = balance
    
#   def Deposit(self,deposit):
#     self.balance = self.balance + deposit
#     return self.balance
  
#   def Withdrawal(self,amount):
#     self.balance = self.balance - amount
#     return self.balance
  
#   def bankFees(self):
#     fees = self.balance*0.05
#     return fees
  
#   def display(self):
#     print(f"Account Number : {self.acc_num}")
#     print(f"Account Name : {self.name}")
#     print(f"Account Balance : {self.balance}")
    

# newAccount = BankAccount(2178514584, "Mandy" , 2800)

# newAccount.Withdrawal(700)

# newAccount.Deposit(1000)

# newAccount.display()