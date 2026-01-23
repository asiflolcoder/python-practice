print("Tuples")
t1 =(12,11,22,11)
# print(t1[0])
# print(t1[-1])
# t1[3]=10
#creating a tuple
# t1 =()
# print(t1)
# t2 =(1)
# print(t2,type(t2))
# t3 = (1,)
# print(t3,type(t3))
# t4 = (12,32,242,244)
# print(t4)
# t5 = ("Asif",24,True,[1,2,3])
# print(t5)
# t6 = (1,2,3,4,(5,6,7))
# print(t6)
# t7 = tuple("Asif")
# print(t7)
# t8 = tuple([1,2,3,5])
# print(t8)

#accessing tuples - indexing,slicing
t1 =("Asif",24,19.99,True,10,20)
# print(t1[0])
# print(t1[-1])
# print(t1[-3])
# print(t1[::])
# print(t1[1:3])
# print(t1[::-1])
# t1[6] ="A"

#editing items
t1 = (12,3,4,2,23,22)
# t1[4] = 22

#adding r editing,deleting korte gele type error dekhai
#deleting items
# del t1[2]
# del t1
# print(t1)
#operation on tuple
#arithmetic - + ,*
t1 = (1,2,3)
t2 = (1,2,3)
# print(t1+t2)
# print(t1*3)
#membership - in,not in
# print(1 in t1)
# print(10 not in t1)
# print(5 in t2)
# print(1 not in t2)
# print(t1 == t2)
# print(t1 is t2)
# for i in t1:
#   print(i)

# t1 = (1,2,3,(10,20),(30,40),(50,60))
# for i in t1:
#   if isinstance(i,tuple):
#     for j in i:
#       print(j)
#   else:
#     print(i)

#tuple functions - max,min,len,sorted,sum
t1 =(1,2,3,4,5,6)
t2 =("Asif",24,True,19.99)
# print(max(t1))
# print(max(t2))
# print(min(t1))
# print(min(t2))
# print(len(t1))
# print(len(t2))
# print(sorted(t1,reverse=True))
# print(sorted(t2))
# print(sum(t1))


#tuple revise
# tu = (12,34,22)
# tu[0] = 10
# print(tu)
tu =("Asif",24,12,12)
# print(tu[0])
# print(tu[1])
# print(tu[2])
# print(tu[3])

#creating a tuple
# t1 = ()
# print(t1,type(t1))
# t2 = ("Asif")
# print(t2,type(t2))
# t3 = (23,)
# print(t3,type(t3))

# #homo 
# t4 = (10,20,30,40)
# print(t4)
# #hetaro
# t5 = ("Asif",24,True,[1,2,3])
# print(t5)
# #2D
# t6 = ("Asif",24,(1,2))
# print(t6)
# #tuple constructor
# t7 = tuple("Asif")
# print(t7)
# t8 = tuple((10,20,30))
# print(t8)

#accessing items-indexing,slicing
t1 = ("Asif",24,True,[1,2,3])
# print(t1[0])
# print(t1[-1])
# print(t1[len(t1)-3])

# print(t1[::])
# print(t1[::-1])
# print(t1[0:3])
# print(t1[-4:])
# print(t1[-5:-4:-1])

#editing items-cannot edit because tuple is immutable
# tu = (10,20,30,40)
# tu[0] = 100
# print(tu)
#adding items is not possible
# tu = (1,2,3,4)
# tu[10]=10

#deleting items
# t = (10,20,30,40)
# del t
# print(t)

#operations on tuple
t1 = (10,20,30)
t2 = (10,20,30)
# print(t1 + t2)
# # print(t1 * t2)
# print((10,20)* 5)
# print(t1 == t2)
# print(t1 == t2)
# print(5 in t1)
# print(10 in t1)
# print(5 not in t1)
# for i in t1:
#   print(i)

#tuple functions- max/sum/min/max/len/sorted
# t1 = (12,3,4,2,5)
# t2 = ("Asif","Probin","Emon")
# print(len(tu))
# print(max(t1))
# # print(max(t2))
# print(min(t1))
# # print(min(t2))
# print(sum(t1))
# # print(sum(t2))
# print(sorted(t1,reverse=True))
# print(sorted(t2))

# print(t1.count(2))

# t1 = (10,20,30,40,30)
# print(t1.count(30))
# print(t1.index(50))

t1 = (10,20,("Asif","Probin"),(1,2,3),(20,30,40))
# for i in t1:
#   for j in t1:
#     if isinstance(j,tuple):
#       print(j)
#   print(i)
# for item in t1:
#   if isinstance(item,tuple):
#     for j in item:
#       print(j)
#   else:
#     print(item)
# t2 = ("Asif",(10,20),(1,2,3),[5,10,15])
# for i in t2:
#   if isinstance(i,tuple or list):
#     for j in i:
#       print(j)
#   else:
#     print(i)

#list vs tuple