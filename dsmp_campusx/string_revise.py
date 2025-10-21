print("String and methodss")
#string creation
# str1 = 'Hello Python'
# str2 = "My name is Asif"
# str3 = """Tripple quoted strings
# Hi I am Someone"""
# print(str1,str2,str3,end='\n',sep='\n')
# print('I am 24 year\"s old')
# num1 = 24
# s1 = str(num1)
# print(s1,type(s1))

#accessing characters in a string

# print(str1[1])
# print(str1[0])
# print(str1[2])
# print(str1[4])
# print(str1[20])
# print(str1[-1])
# print(str1[len(str1)-4])
# print(str1[-4])
# print(str1[len(str1)-6])

str1 = "Hello Python"
#string slicing [::]
# print(str1[:])
# print(str1[1:5])
# print(str1[3:])
# print(str1[1:5:2])
# print(str1[::-1])
# print(str1[-5:])

#string is immutable - particular value change kora jai na ,notun string toiri hoy
# s1 = str1[1:4]
# print(s1)
# str[1:4] ="Asi"
# for x in str1:
#   print(x)
str1 ="Hello Bangladesh"
# for i in range(len(str1)):
#   print(str1[i])
# print(str1)
# del str1[1:4]
# del str1
# print(str1)

#update a string
# s = "Aello Asif"
# s1 = "H"+s[1:]
# print(s1)
# s2 = s.replace()

#operators in string - concatenation(+),multiplication(*),membership 
# print("MD Asif"+" "+"ul Haque")
# age = 24
# # print("I am"+years old")
# print("Hi"*5)

# print("Hi" in "Hi Bangladesh")

#relational operator on string
# s1 = "Asif"
# s2 = "Probin"
# print(s1 > s2)
# print("cat">="CAT")
# print("Mumbai" < "Pune")
# print("Pune" <= "PUNE")
# print("Mumbai"=="MUMBAI")
# print("Mumbai"=="Mumbai")

#logical operator on string

# print("Asif" and "Hasan")
# print(0 and "Asif")
# print("Asif" or "Asifa")
# print(False or "Asif")
# print(not "Asif")
# print(not True)

# print(not "")

#membership - in/not in
# print("D" in "Delhi")
# print("D" not in "Asif")
# print("A" not in "Asif")

#string methods-min,max,len,sorted
str1 = "Hello Bro"
# length = len(str1)
# print(length)

# upper = str1.upper()
# print(upper)

# lower = str1.lower()
# print(lower)

# min_char = min(str1)
# print(min_char)
# print(max("Hello World"))
# print(min("Hello World"))
# str2 = "Bangladesh"
# min_char = min(str2)
# max_char = max(str2)
# print(min_char,max_char)

#capitalize,title,upper,lower
# str1 = "hello asif"
# print(str1.capitalize())
# print("i am 24".capitalize())

# print(str1.title())
# print("i am 24 year old".title())

# print("asif is straight".upper())
# print("Asif is 24 YEARS old".lower())

#strings revise
# s1 = "Hello Python"
# s2 = 'Hello Bro'
# s3 = """
# Hello 
# I am a multiline string
# """

# print(s1,s2,s3)
# print("Hi I am 24 year's old")
# print('I am 24 year"s old')

# s4 = str("23")
# print(s4,type(s4))

#reverse a string
# s1 = "Hello Python"
# for i in range(len(s1)-1,-1,-1):
#   print(s1[i],end="")

#accessing a string-index
s1 = "John Doe"
# print(s1[0])
# print(s1[2])
# print(s1[3])
# print(s1[-1])
# print(s1[-5])
# print(s1[10])
# print(s1[len(s1)-5])
# print(s1[len(s1)-7])

#string slicing[:]- slicing operator
# s1 = "Hello Python"
# print(s1[:])
# print(s1[::-1])
# print(s1[2:4])
# print(s1[1:7:2])
# print(s1[:-5:-1])
# print(s1[-5:])
# print(s1[])

#String and string methods
# str1 = "Hello Python"
# str2 = 'Hello Bro'
# str3 = '''Hello Asif'''
# print(str1,str2,str3,end='\n',sep='\n')

# str4 = "I am 24 year's old"
# str5 = 'I am 24 year"s old'
# multiline_str = """Hi
# I am Asif
# Hi 
# I am Probin
# """
# print(str4)
# print(str5)
# print(multiline_str)

# num = 24
# num_str = str(num)
# print(type(num_str))

#accessing charaters in string - index
# s1 = "Hello Bangladesh"
# print(s1[0],s1[7])
# # print(s1[18])
# print(s1[len(s1)-5])

#slicing -[::](slicing operator)
# s1 = "Hello Bangladesh"
# s2 = s1[1:5:1]
# print(s2)
# s3 = s1[:6]
# print(s3)
# s4 = s1[::]
# print(s4)
# s5 = s1[::-1]
# print(s5)
# print(s1[:])
# print(s1[:6:-1])

# s1 = "Hello Python"
# print(s1[-5:])
# print(s1[-5:-4])
# print(s1[-7:-4])
# print(s1[-11:-5])

#string iteration
# s1 = "I am Asif"
# for x in s1:
#   print(x)

# for i in range(len(s1)):
#   print(s1[i])

# for i in range(len(s1)-1,-1,-1):
#   print(s1[i])

#edit and delete a string
# s1 = "hello Asif"
# # s1[4] = "A"
# print(s1)
# del s1
# print(s1)

#operators on string
#arithmetic - +,*
#concatenation = +
# f_name ="Md Asif"
# l_name ="ul Haque"
# full_name = f_name + l_name
# print(full_name)
# print("Bheramara"+","+"Kushtia")
# print("Asif"+"23")

#multiplication = *
# print("Hi"*5)
# print("Hello world"*10,sep='-')

#relational operator/comparison operator
# print("Asif" > "Probin")
# print("Asif" >="asif")
# print("Dhaka" < "Rajshahi")
# print("Book" <= "Pen")
# print("Mumbai" < "Delhi")
# print("Mumbai" < "Pune")
# print("Pune">'pune')
# print("Asif" < "asif")
# print("pune"<"rajastan")
# print("Asif"=="asif")
# print("Asif"=="Asif")
# print("Mumbai"!="Delhi")
# print("")

# print("Asif" and "Probin")
# print("" and "Emon")
# print("Asif" or "Setu")
# print("" or "Asif")

# print("")
# print(not "")
# print(not "Asif")
# print("Hi" or "bangladesh")
# print(False and "Python")
# print("Java" and "Script")
# print(False or "True")

#membership operator - in/not in
# print("D" in "Delhi")
# print("d" in "Delhi")
# print("a" not in "Asif")
# print("b" not in "boss")

s1 = "Hello Asif"
print(max(s1))
print(min(s1))
print(len(s1))