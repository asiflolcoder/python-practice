print("Hello OOP")

# def sum(a,b):
#   return a + b 

# print(sum(10,20))

# seller1_name = "MD Asif"
# seller1_id = 2323
# seller1_address = '23 street , Bangalore'

# seller2_name = "MD Emon"
# seller2_id = 2324
# seller2_address = '24 street , Bangalore'


# seller1 = ["Asif",2323,"23 street,Bangalore"]

# #seller1.method()

# a = 30
# print(type(a))

# class Car:
#   pass

# volvo = Car()
# print(volvo)
# print(type(Car))

# class Student:
#   def __init__(arg1):
#     name = "Asif"
#     id = 2323
#     print(id(arg1))
#     print("Student class is called")
    
# s1 = Student()
# print(id(s1))

class Student:
  def __init__(self,name,id,profession):
    self.name = name
    self.id = id
    self.is_student = profession
    print("Object is created")
    print(f"name is {self.name} id is {self.id} profession is {self.is_student}")
    
s1 = Student("Asif",2323,"Student")
s2 = Student("Arfi",3433,"Baby")
print(s1.name,s1.id,s1.is_student)
print(s2.name,s2.id,s2.is_student)