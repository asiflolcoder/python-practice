# class Car:
#   pass

# audi = Car()
# print(audi)

class Atm:
  def __init__(self):
    self.pin =''
    self.balance = 0
    self.menu()
    # print(f"pin is {self.pin} and balance is {self.balance}")
    
  def menu(self):
    user_input = input("""
    Hi 
    What you want to do?
    1.press 1 to create pin
    2.press 2 to change pin
    3.press 3 to check balance
    4.press 4 to withdraw balance
    5.press 5 to exit
    """)
    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
      
    
  def create_pin(self):
    user_input =input("Enter a pin:")
    self.pin = user_input
    user_balance = int(input("Enter your balance:"))
    self.balance = user_balance
    print("Pin created successfully")
    self.menu()
    
  def change_pin(self):
    pin = input("Enter your pin:")
    if self.pin == pin:
      new_pin = input("Enter new pin:")
      self.pin = new_pin
      print("Pin updated successfully")
    else:
      print("Wrong Pin")
    self.menu()
    
  def check_balance(self):
    pin = input("Enter your pin:")
    if self.pin == pin:
      
     
  
  
obj = Atm()

  