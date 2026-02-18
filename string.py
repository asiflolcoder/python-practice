print("String and methods")

# s1 = 'Hello Asif'
# s2 = "Hello Emon"
# s3 = """I am 
#       24 years old"""

# print(s1,s2,s3)
# s4 = str(2443.4)
# print(s4,type(s4))

# print("Hi i am 30 year's old")
# print('Hlw How are "you"')

#accessing stings-indexing.slicing
s = "Hello Python"
# print(s[0])
# print(s[6])
# print(s[-1])
# print(s[len(s)-6])

# print(s[15])

#slicing
# print(s[::])
# print(s[::-1])
# print(s[0:6:2])
# print(s[1:5])
# print(s[-1:-5:-1])
# print(s[-1::])
# print(s[-6:])
# print(s[-5:-1])

#editing and deleting strings
# s[0] ="A"
# s1 = s[0]
# print(s1)
# s2 = s[1:4]
# print(s2)
# del s[0]
# del s[0:5]
# del s
# print(s)

#operations on string
# print("Asif"+" "+"Arfi")
# print("Delhi"+ "Mumbai")
# print("Asif"*3)
# print("Asif"-23)
# print("*"*50)
# print("Asif">"Cinema")
# print("Emon">)

#relational operator
# print("Asif"=="Asif")
# print(12 == 12.00)
# print("Dhaka"!="dhaka")
# print("Asif">"Asif")
# print("Asif"<"Emon")
# print('qwer'>="1234")

# print("Asif" and "Afiya")
# print("" and "A")

# print("Asif" or 12)
# print(False and "Asif")

# print(not "")
# print(not "Asif")

# for i in "Hello World":
#   print(i)
  
# s = "Asif is 24 years old"
# for i in range(0,len(s)):
#   print(s[i])

#functions-len,min,max,sorted
s = "Hello Asif"
# print(len(s))
# print(max(s))
# print(min(s))
# print(max(''))
# print(sorted(s,reverse=True))

#more functions - capitalize,title,upper,lower,swapcase
s = "hello WoRld"
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())

#count/index/find
# print(s.count('o'))
# print(s.count('l'))
# # print(s.index("7"))
# print(s.find('w'))
# print(s.find(''))

#find the length

# s = input("Enter a string:")

# count = 0
# for i in s:
#   count +=1
#   print(i)

# print("length is:",count)

# s = input('Enter email:')

# username = ""
# for i in s:
#   if i =="@":
#     break
#   else:
#     username +=i
  
# print("username:",username)

# s = input("enter a string:")
# c = input("enter a character:")
# count =0
# for x in s:
#   if x == c:
#     count +=1
    
# print(c," count:",count)

# s = input("enter the string:")
# c = input("enter the character to remove:")

# str1 = ""

# for x in s:
#   if x ==c:
#     continue
#   else:
#     str1+=x
    
# print("modified string:",str1)


#string revise
# s1 = 'Hello Asif'
# s2 = "Hello Python"
# s3 = """Hi
#   i am asif"""
# print(s1,s2,s3)
# print("Hello I am 24 year's old")
# print('Hello "Probin ')
# s1 = str(2+3j)
# print(s1)

#accessing string - index,slicing
s1 = "Hello Bangladesh"
# print(s1[0])
# print(s1[-4])
# print(s1[len(s1)-3])
# print(s1[1:4])
# print(s1[::-1])
# print(s1[::])
# print(s1[:4])
# print(s1[-1:-5:-1])

#string is immutable - can't edit the string
s1 = "Hello Bangladesh"
# s1[0] = "As"
# print(s1)
# s1[1:3] = "Asif"
# print(s1[0])
# del s1[0] 
# del s1
# print(s1)
#operations on string
#arithmetic - +/*
s1 = "Hello"
# print(s1*3)
# print(s1 + "Asif" + 23)
# print("Mumbai"+"Delhi")
# print("Asif"+"Asif")
#relational - <,<=,>=,>,==,!=
# print("Asif">"Himel")
# print("Asif"<"probin")
# print("Boss" == "Boss")
# print("Boss">"Asif")
# print("Asif"!="asif")
# print("Cat">"Catch")
# print("cat">"CAT")
#string formatting
# name = "Asif"
# age = 24
# print(f"My name is {name} and age is {age}")
# str1 ="My name is {} and age is {}".format(name,age)
# print(str1)

# print("Asif" and "Hasan" and "Probin")
# print("" and "Asif" and "9")
# print("Asif" or False)
# print("" or "AS")
# print(not "Asif")
# print(not "")
# for i in "Hello World":
#   print(i)

# for i in range(1,11):
#   print(f"Hello World {i}")

#membership operator - in,not in
# print("H" in "Hello")
# print("D" in "delhi")
# print("a" not in "Asif")

#common function - len,max,min,sorted
s1 = "hello world"
# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sorted(s1,reverse=True))
# print(s1.capitalize())
# print(s1.title())
# print(s1.upper())
# print(s1.lower())
# print(s1.swapcase())
# print(s1.count("o"))

#find the length of a given string
# s = input("Enter a string:")
# counter = 0
# for i in s:
#   counter += 1
  
# print(f"length of string is : {counter}")

# email = input("Enter your email:")

#string revise

# str1 = 'Hello Asif'
# str2 = "Hello Python"
# str3 ="""Multiline
# string"""
# print(str1,str2,str3)
# print("Asif 's")
# print('Asif"ssf')
# str1 = str("Asif")
# print(str1)
s1 = "Hello Python"
# print(s1[4])
# print(s1[-4])
# print(s1[len(s1)-3])
#slicing - [::]
# print(s1[1:5])
# print(s1[::-1])
# print(s1[::])
# print(s1[:5])
# print(s1[-3:-5:-1])

#s1[0] ="A"
# s2 = s1[0:4]
# print(s2)
# s = "Asif"
# # del s[0]
# del s
# print(s)
#operations on string
