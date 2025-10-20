# email = input("Enter email:")
# password = input("Enter password:")
# if email =="abc@gmail.com" and password== '1234':
#   print("Welcome")
# else:
#   print("Not correct")

#min of three numbers
# int1 = int(input("1st num:"))
# int2 = int(input("2nd num:"))
# int3 = int(input("3rd num:"))

# if int1 < int2 and int1 < int3:
#   print(int1," is smallest")
# elif int2 < int3:
#   print(int2," is smallest")
# else:
#   print(int3," is smallest")

#menu driven calculator
# f_num = int(input("Enter the 1st number:"))
# s_num = int(input("Enter the 2nd number:"))
# op = input("Enter the operation:")
# if op == '+':
#   print(f_num+s_num)
# elif op == '-':
#   print(f_num-s_num)
# elif op == '*':
#   print(f_num * s_num)
# else:
#   print(f_num/s_num)

# menu = input("""
# Hi!how can i help you?
# 1.Enter 1 for pin change
# 2.Enter 2 for balance check
# 3.Enter 3 for withdrawl
# 4.Enter 4 for exit
# """)
#have to create this with oop

#number guessing game
# import random
# r_num = random.randint(1,10)
# print(r_num)
# u_num = int(input("Enter a number:"))

# attempt = 1
# while r_num != u_num:
#   if r_num>u_num:
#     print("guess is less")
#   else:
#     print("guess is higher")
#   u_num = int(input("Enter number again:"))
#   attempt +=1
# else:
#   print("Right guess at attempt:",attempt)

# curr_pop = 10000
# for i in range(10,0,-1):
#   print(i,curr_pop)
#   curr_pop = curr_pop - (0.1* curr_pop)
  