# print("Getting started")
# message = "Hello Python"
# print(message)
print("Python data types and variables")
# int_var = 10
# float_var = 34.56
# str_var = "Asif"
# bool_var = True
# print(int_var,type(int_var))
# print(float_var,type(float_var))
# print(str_var,type(str_var))
# print(bool_var,type(bool_var))
#assigning multiple values
# a,b,c = 10,"Python",False
# print(a,b,c)
# print(id(a),id(b),id(c))
# a=b=c=10
# print()
dig = 7895
ls =[]
while dig!=0:
  last_dig = dig % 10
  ls.append(last_dig)
  dig = dig //10

print(ls)