class Customer:
  def __init__(self,name,gender,address):
    self.name = name
    self.gender = gender
    self.address = address
  
  def print_address(self):
    print(self.address.city,self.address.pin,self.address.division)
    
class Address:
  def __init__(self,city,pin,division):
    self.city = city
    self.pin = pin
    self.division = division
    
add1 = Address("Kushtia",7040,"Khulna")
cust1 = Customer("Asif","Male",add1)
cust1.print_address()