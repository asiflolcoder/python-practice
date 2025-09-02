print("String and methods - Tutorialspoint")

str1 = 'Hi I am Python'
str2 = "I don't love Bangladesh"
str3 = '''I love Python'''
# print(str1,type(str1))
# print(str2,type(str2))
# print(str3,type(str3))
 
# print(str1[0],str1[1])
# print(str2[1],str2[4])

# for character in str1:
#   print(character,end=" ")
# for x in str2:
#   print(x,end='-')

str1 = "Hello World!"
print(str1)
#escape characters
# print("I am 24 year\'s old")
# print("Hi i am Asif\nI am 24\nI live in Rajshahi")
# print("Tab will appear as \tinc")
# print("Backspace is \bii")

#string slicing

# print("length is :",len(var))
# print(var[0])
# print(var[11])
# print(var[12])
# print(var[len(var)-3])
# print(var[len(var)-1])
# print(var[len(var)-5])
# print(var[len(var)-12])

# var = "Hello Python"
# print(var[1:5])
# print(var[:8])
# print(var[len(var)-9:len(var)-4])

#string modifying using a list
# str = "Hello Asif"
# l = list(str)
# print(l)

# l[0] ="I"
# l[1] = " "
# l[2] = "a"
# l[3] ="m"
# print(l)
# s1 = str(l)
# print(s1)\

# s1 = "WORD"
# print("Original string:",s1)
# li = list(s1)
# li.insert(3,"L")
# print(li)
# s1 =""
# s2=s1.join(li)
# print(s2)

# import array as ar
# s1 = 

#string concatenation
# f_name = "Md Asif"
# l_name = "ul Hauqe"
# print(f_name+" "+l_name)

# str1 = "abc"
# print(str1*10)
# # print("Asif"+23)

# str1 ="Hello"
# str2 = "World"
# str3 = str1+" "+str2
# print(str3)

# #string repetition
# h1 = "Hello"
# print(h1 *3 )

# s1 = "I love"
# s2 = "Python"
# concat = s1 + " " + s2
# print(concat * 3)

#string revise
str1 = 'Hi i am Python'
str2 = "Hello Bro"
str3 = '''Good Morning'''

print(str1[0]) 
print(str2[0]) 
print(str3[3]) 

# str[0] = "I"
# str1 = "str1 updated"
# print(str1)

# #escape characters
# print("Multiline\nI am 24 year\'s old\n\"I am a student\"")

#string slicing
str = "Hello Python"
# s1 = str[:]
# print(s1)
# s1 = str[0:5]
# print(s1)
# print(str[len(str)-1:len(str)-4])
# print(str[1:10:2])
# print(str[10:2])
# print(str[-8:-3])
#string modification 
str = "I want to go to America"
str_li = list(str)
# print(str_li)
str_li[0] ="H"
str_li[1] ="e"
str="".join(str_li)
print(str)

import array as ar
s1 = "Hello Bangladesh"
sar =ar.array('u',s1)
print(sar)