print("Hello Loops from tutorialspoint")
#3 types - while,for,nested
# li = [12,34,21,22,1]
# for x in li:
#   print(x)
  
# str ="Hello Python From Tutorialspoint"
# for x in str:
#   print(x,end=" ")
  
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
# for char in zen:
#   if char is not 'aeiou':
#     print(char,end=' ')

# numbers = (12,34,22,11,98)
# total=0
# for x in numbers:
#   total+=x

# print("Sum is:",total)

# li = [12,23,11,34,22,77,42]
# for x in li:
#   if x%2==1:
#     print(x,end='-')

# for i in range(1,10,1):
#   print(i)
  
# for i in range(0,20,2):
#   print(i)

# for i in range(5):
#   print(i,end=" ")
# print()
# for i in range(10,20):
#   print(i,end=" ")
# print()
# for i in range(1,10,2):
#   print(i,end=" ")

#loop with dictonaries
dic = {"name":"Md Asif","age":24,"is_student":True}
# for x in dic:
#   print(x)
  
# for key in dic:
#   for value in dic:
#     print(key[value])
# for x in dic:
#   print("keys are:",x)
#   print("values are:",dic[x])

# for key in dic:
#   print(key,":",dic[key])

#check prime number
for num in range(20,40):
  for i in range(2,num):
    if num%i==0:
      j = num/i
      print("%d equals to %d * %d" %(num,i,j))
      break
    else:
      print("%d is a prime number" %(num))
      break
  