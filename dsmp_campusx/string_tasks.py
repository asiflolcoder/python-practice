#reverse a string
# s1 = "Hello Python"
# for i in range(len(s1)-1,-1,-1):
#   print(s1[i],end="")

#palindrome check
s1 = "madame"
l1 = []
for i in range(len(s1)-1,-1,-1):
  l1.append(s1[i])
s2 = "".join(l1)
if(s1==s2):
  print("True")
else:
  print("False")

#specific character appearing
# s1 = "Banana"
# char = "a"
# counter = 0
# for x in s1:
#   if(x == char):
#     counter+=1
# print(counter)

#string to title case
# s1 = "welcome to python"
# title_case = s1.title()
# print(title_case)

s1 = "welcome to python"



#