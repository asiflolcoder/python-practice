print("variable","&","Data type",sep=" ")
num1 = 20
print(id(num1))
counter = 1000
price = 23.455
can_vote = False

# print(counter)
# print(price)
# print(can_vote)
# del price
# print(price)
#multiple assignment
# name,age,price = "Asif",24,25.99
# print(id(name),type(name),name)
# print(id(age),type(age),age)
# print(id(price),type(price),price)

# a=b=c = 100
# print(id(a),id(b),id(c))

#local variable - cannot be accessed outside function
# def sum():
#   a=10
#   b = 20
#   c = a+b
#   return c

# print(a,b)

#global variable 
# x = 10
# y = 15
# def sub():
#   c = x - y
#   return c

# print(sub())

#data types 
#numeric - int,float,complex,bool
# var1 = 100
# var2 = 23.45
# var3 = True
# var4 = 3 + 4j

#variable  and data type revise

name = "Hello Asif"
age = 24
is_student = False
price = 39.99
print(name,age,is_student,price)
# del age 
# print (age)

#local variables
# def sum():
#   a= 10 
#   b = 20
#   print(a+b)
# sum()

# print(a+b)
 
# #global variable
# a = 20
# b = 30
# def multi():
#   c = a * b
#   print(c)
# multi()

# PI_VALUE = 3.14422314

#numeric data type
int_var = 23242
float_var = 223.9838
bool_var = True 
complex_var = 3 + 4j
print(type(int_var))
print(type(float_var))
print(type(bool_var))
print(type(complex_var))

str1 = 'Asif'
str2 = "Emon"
str3 = '''Probin'''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))

l = [12,"Asif",True,23.99]
for x in l:
  print(x)
  
