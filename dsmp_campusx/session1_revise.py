import sys
print("Session 1 revise")

# print("Hello World")
# print("Hello","I am",24)
# print("Asif",False,23.4,sep='-')
# print("Asif",False,23.4,sep=' ')
# print("Asif",False,23.4,sep=' ',end='\n')
# print("session1",end='/')

#numeric type
# num1 = 234
# num2 = 342425252242424
# print(sys.getsizeof(num1))
# print(sys.getsizeof(num2))
# print(type(num1),type(num2))

# flo1 = 231.2323
# flo2 = 3424424241.242424242
# print(sys.getsizeof(flo1))
# print(sys.getsizeof(flo2))
# print(type(flo1),type(flo2))
# bool1 = True
# bool2 = False
# print(sys.getsizeof(bool1))
# print(type(bool2))

# complex1 = 3 + 4j
# print(sys.getsizeof(complex1))
# num1 = complex(3,4)
# print(num1)

#sequence type - list,tuple,string
# li = [23,"Asif",True]
# print(li,type(li))
# str = "hello python"
# print(str,type(str))

# tu = (23,22,11,"Asif")
# print(tu,type(tu))

# set1 = {23,"Asif",True}
# print(set1,type(set1))

# dict1 = {"name":"Asif"}
# print(dict1,type(dict1))

# num1 = None
# print(num1,type(num1))

#dynamic binding
# a = 3422
# print(a)
# a = "Asif"
# print(a)
# b,c,d = 23,22,1
# print(b,c,d)
# a=b=c= 100
# print(id(a),id(b),id(c))

#keywords and identifier
# 1ab = 23
# ab1 = 23
# ab_23 = 2322

# # input1 = input("")

# input1 = int(input("Enter a number:"))
# input2 = int(input("Enter a number:"))
# sum = input1 + input2
# print(sum)


#type conversion
# print(10+10.5) #implicit
# num1 = int("23")
# print(num1)
# print(34+"34")

#literals
# a = 2 
# print(a)
# a = 0b1010
# print(a)
# a= 0o423
# print(a)
# a = 0x12c
# print(a)

# a = 22e10
# print(a)

# f = 12.342
# print(f)
# f = 232.23e2
# print(f)
# f = 211.e-3
# print(f)

# str1 = 'Hello Python'
# print(str1)
# str1 ="Hello Bro"
# print(str1)
# str1 = """Triple quotes"""
# print(str1)

# print("escape characters\n \\ \'")

#complex literals
# complex1 = 3 + 4j
# complex2 = complex(4,3)
# print(complex1,complex2)

#boolean
# bool1 = True
# bool2 = False
# print(bool1,int(bool1))
# print(bool2,int(bool2))

# a = True + 1
# print(a)

# b = False - 0
# print(b)

# a = None
# print(a)


#tasks - chatgpt
#age calculator
# birth_year = int(input("Enter birth year:"))
# current_year = 2025
# current_age = current_year - birth_year
# print(f"You are {current_age} years old")

#temperature converter
# celcius = float(input("Enter celcius temperature:"))
# fahrenheit = celcius * (9/5) + 32
# print(f"celcius:{celcius} fehrenheit:{fahrenheit}")

#bill splitter
# total_bill = float(input("Enter total amount:"))
# num_of_frnds = int(input("Enter number of friends:"))
# pay = total_bill/num_of_frnds
# print(f"one should pay {pay}") 

#rectangle area
# length = float(input("enter length:"))
# width = float(input("enter width:"))
# area = length * width
# print(f"area is : {area}")

#string joiner
# first_name = input("enter first name:")
# last_name = input("enter last name:")
# full_name = first_name + " " + last_name
# print(f"Hello {full_name}")


#printing string
# print("Data","Science","Mentorship","Program","started","By","CampusX",end='\n',sep='-')

# simple interest calculator
# principle = float(input("Enter principle amount:"))
# rate = float(input("enter interest rate:"))
# time = float(input("Enter years :"))
# interest = (principle * rate * time)/100
# print(f"Interest :{interest}")

#bmi calculator
# weight = float(input("Enter weight in kg:"))
# height_feet = float(input("enter height in feet:"))
# height = height_feet * 0.3048
# BMI = weight / (height**2)
# print(f"BMI is:{BMI:0.2f}")

#number swapper
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))

# num1,num2 = num2,num1
# print(num1,num2)


#discount calculator
# original_price = float(input("Enter price:"))
# discount_amount = float(input("Enter discount amount:"))/100
# final_price= original_price - (original_price*discount_amount)
# print(f"After discount :{final_price}")

#seconds to hours
# seconds = int(input("Enter seconds:"))
# minutes = seconds % 60 
# second = seconds - minutes
# print(f"{minutes} minutes {second} seconds")

#data summary
# num1 = float(input("Enter a number:"))
# num2 = float(input("Enter a number:"))
# num3 = float(input("Enter a number:"))
# sum = num1 + num2 + num3
# average = (num1 + num2 + num3)/3
# max_num = max(num1,num2,num3)
# min_num = min(num1,num2,num3)
# print(f"sum:{sum} average:{average} maximum:{max_num} minimum:{min_num}")

#student info formatter
# stu_name = input("Enter student name:")
# age = int(input("Enter age:"))
# gpa = float(input("Enter gpa:"))
# print(f"Student: {stu_name}")
# print(f"Age: {age}")
# print(f"GPA: {gpa}")

#salary breakdown
# monthly_salary = float(input("enter monthly salary:"))
# yearly_salary = monthly_salary * 12
# tax_amount = yearly_salary * 0.1
# net_income = yearly_salary - tax_amount
# print(f"yearly salary:{yearly_salary} tax:{tax_amount} net income:{net_income}")

#currency converter
# amount_bdt = int(input("Enter amount in BDT:"))
# usd = amount_bdt / 121.38
# inr = amount_bdt / 1.37
# print(f"USD:{usd:0.2f}")
# print(f"INR:{inr:0.2f}")

