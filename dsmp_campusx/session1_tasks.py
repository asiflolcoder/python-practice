# Q1 :- Print the given strings as per stated format.
# Given strings:

# "Data" "Science" "Mentorship" "Program" 
# "By" "CampusX"

# print("Data","Science","Mentorship","Program","Started","By","CampusX",sep="-",end='')

# Q2:- Write a program that will convert celsius value to fahrenheit.
# Write your code here
# celcius = int(input("Enter celcius value:"))
# farenheit = ((9/5)*celcius)+32
# print("Temerature in fahrenheit:",farenheit)

# Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
# Write your code here
#input from users
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))
# #swap the numbers
# temp = num1
# num1 = num2
# num2 = temp
# #print the numbers
# print("After swapping:",num1,num2)


# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.
# Write your code here
#input from user
# x1 = int(input("Enter x1:"))
# y1 = int(input("Enter y1:"))
# x2 = int(input("Enter x2:"))
# y2 = int(input("Enter y2:"))
# #calculating the distance
# distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
# #printing the value
# print("Distance:",distance)

# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

#input from user
# p = int(input("Enter principle value:"))
# r = float(input("Interest rate:"))
# t = int(input("Enter time period:"))
# #calculate the interest
# interest = (p * r * t)/100
# #print the value
# print("interest is:",interest)


# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
input from user
head = int(input("Enter amount of heads:"))
leg = int(input("Enter amount of legs:"))
#calculation
dog =

# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
#input from user
# num = int(input("Enter a number:"))
# sum = 0
# for i in range(1,num+1):
#   sum = sum + (i*i)

# # print("Sum is:",sum)
# sum = (num * (num + 1) * (2*num + 1))/6
# print("sum is:",sum)

# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
# num1 = int(input("Enter 1st number:"))
# num2 = int(input("Enter 2nd number:"))
# diff = num2 - num1
# n = int(input("nth term:"))

# l = num1 + (n - 1)* diff 
# print("n th term:",l)

# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
# num1 = float(input("Enter numerator:"))
# den1 = float(input("Enter a denominator:"))

# num2 = float(input("Enter numerator:"))
# den2 = float(input("Enter a denominator:"))

# sum = (num1 * den2 + num2 * den1)/(den1 * den2)
# print("Sum of two fraction:",sum)

# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

import math
height = float(input("Enter height:"))
width = float(input("Enter width:"))
breadth = float(input("Enter breadth:"))

vol = height * width * breadth

glass_h = float(input("Enter glass height"))
glass_r =float(input("Enter glass radius"))
glass_v = math.pi * glass_h * (glass_r**2)

glass_num =math.floor(vol / glass_v)
print("number of glasses:",glass_num)