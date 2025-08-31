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

l1 = ["a","b","c","d","e"]
l2 = [2,4,5]
# l1[0:4]=l2
# print(l1)
l1[1:3]=l2
print(l1)

#adding a element in last
fruits = ["Apple","Banana","Mango","Date"]
fruits.append("Watermelon")
print(fruits)

fruits.insert(0,"Dragon Fruit")
fruits.insert(3,"Berry")
print(fruits)

id = [2323,1232,4231]
names =["Asif","Probin","Emon"]
id.extend(names)
print(id)

list1 = [1,2,3,4,5]
list2 = [10,20,30,40]
list1.extend(list2)
print(list1)
