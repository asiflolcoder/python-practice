print("Python object oriented programming")

# l = [1,2,3]
# l.upper()

#oop - class ,object,encapsulation,inheritance,polymorphism,abstraction

# l = [1,2,3]
# print(type(l))

#class - property/attribute - blueprint of object
# class Student:
#   def __init__(self)

# st1 = Student()
# class Human:
#   def __init__(self):
#     print("Human object created")
    
# asif = Human()

# class Student:
#   def __init__(self):
#     self.name = "Asif"
#     self.age = 25
#     self.course ="CSE"
#     print(f"name:{self.name} age:{self.age} course:{self.course}")

# stu_asif = Student()

# class Student:
#   def __init__(self,name,age,course):
#     self.name = name
#     self.age = age
#     self.course = course
#     print(f"name:{self.name} age:{self.age} course:{self.course}")

# student1 = Student("Probin",24,"EEE")
# student2 = Student("Asif",25,"CSE")
# print(type(student1))
    
# class Atm:
#   def __init__(self):
#     self.balance = 0
#     self.pin =""
#     self.menu()
  
#   def menu(self):
#     user_input=input("""Hi
#           How can i help you?
#           1.Press 1 to create pin
#           2.Press 2 to change pin
#           3.Press 3 to debit balance
#           4.Press 4 to withdraw balance
#           5.Press 5 to check balance
#           6.Press 6 to exit\n""")
    
#     if user_input =="1":
#       self.create_pin()
#     elif user_input =="2":
#       self.change_pin()
#     elif user_input =="3":
#       self.credit_balance()
#     elif user_input =="4":
#       self.withdraw_balance()
#     elif user_input =="5":
#       self.check_balance()
#     else:
#       self.menu()
      
#     self.menu()
      
#   def create_pin(self):
#     user_pin = input("Enter pin:")
#     self.pin = user_pin
#     print("Pin created successfully")
    
#   def change_pin(self):
#     user_pin = input("Enter your pin:")
#     if user_pin == self.pin:
#       new_pin = input("Enter new pin:")
#       self.pin = new_pin
#       print("New pin created")
#     else:
#       print("Wrong pin")
  
#   def credit_balance(self):
#     user_pin = input("Enter your pin:")
#     if user_pin == self.pin:
#       balance = int(input("Enter your balance:"))
#       self.balance = balance
#       print("Balance credited successfully")
#     else:
#       print("Wrong pin")
      
#   def withdraw_balance(self):
#     user_pin = input("Enter your pin:")
#     if self.pin == user_pin:
#       withdraw_balance = int(input("Enter amount to withdraw:"))
#       if withdraw_balance < self.balance:
#         self.balance = self.balance - withdraw_balance
#         print(f"{withdraw_balance} withdrawn successfully")
#         print(f"current balance is:{self.balance}")
#       else:
#         print("You don't have thar much balance")
        
#     else:
#       print("Wrong pin")
    
  
#   def check_balance(self):
#     print("current balance is {}".format(self.balance))
  

# obj = Atm()

# class Student:
#   def __init__(self,name,age,course):
#     self.name = name
#     self.age = age
#     self.course = course

#   def read():
#     print()

# class Car:
#   def __init__(self):
#     print(id(self))
  
#   def __str__(self):
#     print("Object got created")
  
# bmw = Car()
# print(id(bmw))
# # print(bmw)

# class Car:
#   def __init__(Self,name,model):
#     Self.name = name
#     Self.model = model
    
#   def __str__(Self):
#     return f"Car name:{Self.name} model:{Self.model}"

# bmw =Car("BMW","X6")
# print(bmw)
# audi = Car("Audi","R8")
# print(audi)