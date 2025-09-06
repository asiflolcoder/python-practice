# Q-1: Rectangle Class
# Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.


class Rectangle:
  def __init__(self,length,width):
    self.length = length
    self.width = width
    
  def perimeter(self):
    parameter = 2 * (self.length + self.width)
    return parameter
  
  def area(self):
    area = self.length * self.width
    return area
  
  def display(self):
    print("The length of rectangle is:",self.length)
    print("The width of rectangle is:",self.width)
    print("The perimeter of rectangle is:",self.perimeter())
    print("The area of rectangle is:",self.area())
  
my_rectangle = Rectangle(3,4)
my_rectangle.display()

class BankAcount:
  def __init__(self,accountNumber,name,balance):
    self.accountNumber = accountNumber
    self.name = name
    self.balance = balance
    
  def Deposit(self,deposit):
    # self.deposite = deposit
    self.balance = self.balance + deposit
    
  def Withdrawal(self,withdraw):
    self.balance = self.balance - withdraw
  
  def bankFees(self):
    fees = self.balance * (5/100)
    self.balance = self.balance - fees
      
  def display(self):
    print("Account number : ",self.accountNumber)
    print("Account Name : ",self.name)
    print(f"Account Balance : {self.Withdrawal()}")
    

newAccount = BankAcount(2178514584,"Mandy",2800)
newAccount.Withdrawal(700)
newAccount.Deposit(1000)
newAccount.display()