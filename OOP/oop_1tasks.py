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