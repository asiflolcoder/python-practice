print("Everything about list from Tutorialspoint")

# list1 = [12,32,1,2,3,4]
# list2 = ["Asif",True,23.45,2+3j]
# print(list1,list2)

# print(list1[0])
# print(list1[2])
# print(list2[3])

# list1[0] = 100
# list1[1] = 50
# print(list1)

# list2[0] ="Emon"
# list2[3] = 3+4j
# print(list2)

# del list2[0]
# del list2[1]
# print(list2)

# #list concatenation(+)
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1 + l2
# print(l3)

# #list repitition
# l1 = [12,23]
# print(l1*4)

# print(3 in [1,3,4])

#accessing list iteams
# l1 = ["a","b","c","d","e"]
# print(l1[len(l1)-3])
# print(l1[-2])

# #slie operator
# print(l1[1:3])

# print(l2[0:5:2])
# print(l2[1:3])

#change list
# l2 = [12,23,22,11,44,24,4]
# l3 = [100,200,300]
# l2[0:3]=l3
# print(l2)

# l1 = ["a","b","c","d","e"]
# l2 = [2,4,5]
# # l1[0:4]=l2
# # print(l1)
# l1[1:3]=l2
# print(l1)

# #adding a element in last
# fruits = ["Apple","Banana","Mango","Date"]
# fruits.append("Watermelon")
# print(fruits)

# fruits.insert(0,"Dragon Fruit")
# fruits.insert(3,"Berry")
# print(fruits)

# id = [2323,1232,4231]
# names =["Asif","Probin","Emon"]
# id.extend(names)
# print(id)

# list1 = [1,2,3,4,5]
# list2 = [10,20,30,40]
# list1.extend(list2)
# print(list1)

# l1 = [1,2,3,4,5]
# l1.remove(3)
# print(l1)
# l1 = [1,3,3,2,1]
# l1.remove(3)
# print(l1)

# l1 = [23,34,22,11,2]
# # print(l1.pop())
# # print(l1)
# l1.pop(2)
# print(l1)

# l2 = ["Urmi","Monika","Sadia","Mow"]
# # l2.pop()
# # print(l2)
# l2.pop(1)
# print(l2)
# l2.clear()
# print(l2)
# l1.clear()
# print(l1)

# l2 = [12,232,23,112,23,2]
# del l2[0]
# del l2[3]
# print(l2)

# l2 = ["Asif",True,23.44,2+3j]
# del l2[0:2]
# print(l2)

list1 = [23,22,"Asif",True,4.99]
for item in list1:
  print(item,end=' ')
  
index = 0
while index < len(list1):
  print(list1[index])
  index = index + 1
  
  