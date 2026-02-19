print("List and methods")

# l = [10,"Asif",25.99,True]
# print(id(l[0]))
# print(id(l[1]))
# print(id(l[2]))
# print(id(l[3]))

#characteristics of list
# l = [1,2,3,4]
# print(l[1])
# print(l[-1])
# print(l[0])

# l = [12,34,22]
# l[0] = 10
# print(l)

# l = [12,"Asif",23.44]
# print(l)

# l = [12,34,12]
# print(l)
# l.append(100)
# print(l)
# l = [12,10,[12,12]]
# print(l)

# l = [(1,2),"Asif",{"name":"Asif"}]
# print(l)

# ulti_list = [10,[20,30],"Asif",True,(5,6),{"age":24}]
# print(ulti_list[0])
# print(ulti_list[-1])
# ulti_list[0] = 100
# print(ulti_list)
# l1 = [12,3,43]
# l2 = [12,3,43]
# print(l1 == l2)
# print(l1 is l2)

#creating a list
# l1 = []
# print(l1)
# l2 = ["Asif","Probin","Hasan"]
# print(l2)
# l3 = [12,34,[1,2],[2,3]]
# print(l3)
# print(l3[2][0])
# l4 = ["Asif",24,True]
# print(l4)
# l5 = [[1,2,[5,6]],[0,10,[20,30]]]
# print(l5[0][2][0],l5[1][2][1])
# li = list("Asif")
# print(li)
# l1 = list((12,34,55))
# print(l1)
# l2 = list([12,34,[1,2]])
# print(l2)
#accessing items from a list
l = [10,20,30,40,50]
# print(l[0])
# print(l[3])
# print(l[-1])
# print(l[len(l)-4])
# print(l[::])
# print(l[::-1])
# print(l[1:4])
# print(l[0:3])
# print(l[-5:-1:])

#adding items on a list-append,insert,extend
# l = [10,20,30,40,50,60]
# print(l.append(70))
# print(l)
# l.extend("Asif")
# print(l)
# l.extend([1,2,3])
# print(l)
# l.insert(0,'Asif')
# print(l)

# l1 = [10,20,30,40]
# l1.insert(1,200)
# l1.insert(-1,[1,2])
# print(l1)
# l1.append(100)
# print(l1)
# l1.extend("Asif")
# print(l1)

#editing items on a list
# l = [1,2,3,4,5,6,7]
# l[0] = [12,34]
# print(l)
# l[1] = 100
# print(l)
# l[0:3]=[1,2,3]
# print(l)

#deleting items from a list - pop,del,remove,clear
l = [10,20,30,50,40]
# l.pop()
# print(l)
# l.pop(0)
# print(l)
# del l[0]
# print(l)
# del l[0:2]
# print(l)
# print(l.pop())
# l.remove(20)
# print(l)
# print(l.remove(40))
# print(l)
# l.clear()
# print(l)
# print(l)
# del l
# print(l)
# del l[0]
# print(l)
# del l[0:2]
# print(l)
# l.pop()
# print(l)
# l.pop(1)
# print(l)
# l.remove(50)
# print(l)
# l.clear()
# print(l)

#operation on list
#arithmetic - +,*
# l1 = [1,2,3]
# l2 = [4,5,6]
# print(l1+l2)
# print(l1*4)

#list revise
# l = [12,"Asif",True,10,[1,2,3]]
# print(id(l[0]))
# print(id(l[1]))
# print(id(l[2]))

# l[0] = 10
# print(l)
#nested list
# l = [10,20,30,[1,2,3,[5,6]]]
# print(l[3][3][1])
# l = list([1,2,3,4])
# print(l)

#accessing list items- index,slicing
l1 = [10,"Asif",True,(1,2,3)]
# print(l1[0])
# print(l1[-2])
# print(l1[len(l1)-3])

# print(l1[::-1])
# print(l1[::])
# print(l1[1:3])
# print(l1[-1:-3:-1])

#adding items to a list-append,extend,insert
list1 = [10,20,30,40]
# list1.append(50)
# list1.append([1,2,3])
# list1.append(("Asif"))
# list1.append("Asif")
# print(list1)
# list1.extend("Asif")
# print(list1)
# list1.extend([1,2,3])
# print(list1)
# list1.insert(0,"Asif")
# print(list1)

#editing items on a list
#list is mutable - can change any particular value
# l = [10,"Asif",24.5,True,1,2]
# l[0] = 100
# print(l)
# l[1:3]=["Asif"]
# print(l)

#deleting items from a list
# del l[0]
# print(l)
# del l[1:3]
# print(l)
# del l
# print(l)




#problem 1
# list1 = ["M","na","i","Kh"]
# list2 = ["y","me","s","an"]
# list3 = []

# for i in range(0,len(list1)):
#   item = []
#   item.append(list1[i])
#   item.append(list2[i])
#   list3.append(item)

# print(list3)

#problem - 2
# list1 = [10,20,[300,400,[5000,6000],500],30,40]

# for item in list1:
#   if isinstance(i,list):
#     for j in i:
      
  

#problem - 4
# list1 = [1,2,3,4,5,6]
# list2 = []
# sum = 0
# for i in list1:
#   sum +=i
#   list2.append(sum)
  
# print(list2)

#problem - 3
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]

# for i in range(0,len(candy_list)):
#   print(f"{candy_list[i]}- {no_of_items[i]}")

#problem - 10
# list1 = ['campusxIs', 'bestFor', 'dataScientist']
# for item in list1:
#   for char in item:
#     if char.upper() 

#problem - 11
# list1 = [1,2,3,4,5,1]
# list2 = [2,3,5,7,8]
# list3 = []

# for i in range(0,len(list1)):
#   if list1[i] == list2[i]:
#     list3.append(list1[i])
#   else:
#     list3.append(list2[i])

#list revise
