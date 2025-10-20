# class Car:
#   pass

# audi = Car()
# print(audi)

# class Car:
#   def __init__(self):
#     self.brand = "Audi"
#     self.color = "Red"
#     self.seat = 4
#     print('car brand is:{} color:{} seat:{}'.format(self.brand,self.color,self.seat))
  
# Audi = Car()
# ferari = Car()

# class Car:
#   def __init__(self,brand,color,seat):
#     self.brand = brand
#     self.color = color
#     self.seat = seat
#     print(f"{self.brand} car {self.color} color and {self.seat} seats")

# Audi = Car("Mercedes","Black",4)



# class Atm:
#   def __init__(self):
#     self.pin =''
#     self.balance = 0
#     self.menu()
#     print(f"pin is {self.pin} and balance is {self.balance}")
    
#   def menu(self):
#     user_input = input("""
#     Hi 
#     What you want to do?
#     1.press 1 to create pin
#     2.press 2 to change pin
#     3.press 3 to check balance
#     4.press 4 to withdraw balance
#     5.press 5 to exit
#     """)
#     if user_input == '1':
#       self.create_pin()
#     elif user_input == '2':
#       self.change_pin()
#     elif user_input == '3':
#       self.check_balance()
#     elif user_input == '4':
#       self.withdraw_balance()
#     else:
#       exit()
      
    
#   def create_pin(self):
#     user_input =input("Enter a pin:")
#     self.pin = user_input
#     user_balance = int(input("Enter your balance:"))
#     self.balance = user_balance
#     print("Pin created successfully")
#     self.menu()
    
#   def change_pin(self):
#     pin = input("Enter your pin:")
#     if self.pin == pin:
#       new_pin = input("Enter new pin:")
#       self.pin = new_pin
#       print("Pin updated successfully")
#     else:
#       print("Wrong Pin")
#     self.menu()
    
#   def check_balance(self):
#     pin = input("Enter your pin:")
#     if self.pin == pin:
#       print("Current balance is",self.balance)
#     else:
#       print("Your pin is incorrect")
#     self.menu()
    
#   def withdraw_balance(self):
#     pin = input("Enter your pin:")
#     if self.pin == pin:
#       amount = int(input("How much you wanna withdraw:"))
#       if amount< self.balance:
#         self.balance = self.balance - amount
#         print("Balance is:",self.balance)
#       else:
#         print("You don't have that much")
#     else:
#       print("Wrong pin")
#     self.menu()

#   def exit(self):
#     self.menu()
  
# obj = Atm()


#magic methods
# class Student:
#   def __init__(self,name,age,id):
#     # print(id(self))
#     self.name = name
#     self.age = age
#     self.id = id
  
#   def __str__(self):
#     return f"name:{self.name} age:{self.age} id:{self.id}"
  
# student_1 = Student("Asif",24,2323)
# print(id(student_1))
# print(student_1)

#creating our own data type - Fraction
# class Fraction:
#   def __init__(self,num,den):
#     self.num = num
#     self.den = den
    
#   def __str__(self):
#     return ('{}/{}'.format(self.num,self.den))
  
#   def __add__(self,other):
#     new_num = (self.num * other.den + other.num * self.den)
#     new_den = (self.den * other.den)
#     return '{}/{}'.format(new_num,new_den)
  
#   def __sub__(self,other):
#     new_num = (self.num * other.den - other.num * self.den)
#     new_den = (self.den * other.den)
#     return '{}/{}'.format(new_num,new_den)
  
#   def __mul__(self,other):
#     new_num = self.num * other.num
#     new_den = self.den * other.num
#     return '{}/{}'.format(new_num,new_den)
  
#   def __truediv__(self,other):
#     new_num = self.num * other.den 
#     new_den = self.den * other.num
#     return '{}/{}'.format(new_num,new_den)
  
# num1 = Fraction(5,8)
# num2 = Fraction(4,5)
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)
# print(num1)

# complex1 = complex(4,5)
# complex2 = complex(5,6)
# print(complex1 + complex2)