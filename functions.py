#functions and methods
print("Functions")
# def sum():
#   """
#   calculates sum
#   input - no input
#   output - sum of two numbers
#   created by - asif 
#   """
#   a = 10
#   b = 20
#   print(a+b)

# sum()

# print(print.__doc__)
# print(sum.__doc__)
# print(type.__doc__)

# def is_even(num):
#   """
#   fn to calculate even/odd numbers
#   input - any valid integer
#   output - even/odd
#   created - name date
#   """
#   if type(num) == int:
#     if num % 2 ==0:
#       return "Even"
#     else:
#       return "Odd"
#   else:
#     return "Wrong value passed"
# for i in range(1,11):
#   print(is_even(i))

# print(is_even("Asif"))
# print(is_even.__doc__)

# arguments
# def sum (a=10,b=20):
#   return a + b
# print(sum(10))
# def sub(a=0,b=0):
#   return a - b
# print(sub(50,20))

# l = [1,2,3]
# print(l.append(4))

#variable scope
# def g(y):
#   print(x)
#   print(x+1)
# x = 5
# g(x)
# print(x)
# def f(y):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# f(x)
# print(x)
# def h(y):
#     x += 1
# x = 5
# h(x)
# print(x)

# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = []
# for i in l1:
#   if i % 2 ==0:
#     l2.append(i)
# print(l2)

# def outer():
#   print("outer function")
#   def inner():
#     print("inner function")
#   inner()
# outer()
# inner()
# def g(x):
#     def h():
#         x = 'abc'
#     x = x + 1
#     print('in g(x): x =', x)
#     h()
#     return x

# x = 3
# z = g(x)
# print(z)

# def g(x):
#     def h(x):
#         x = x+1
#         print("in h(x): x = ", x)
#     x = x + 1
#     print('in g(x): x = ', x)
#     h(x)
#     return x

# x = 3
# z = g(x)
# print('in main program scope: x = ', x)
# print('in main program scope: z = ', z)
# l1 = [1,2,3,3,3,3,4,5]
# l2 = []
# for i in range(len(l1)-1,-1,-1):
#   for j in range(0,i):
#     if l1[i] == l1[j]:
#       continue
#     else:
#       l2.append(l1[j])
# print(l2)
    
