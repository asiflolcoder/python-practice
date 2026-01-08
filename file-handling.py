#if file is not present
# f = open('./sample.txt','w')
# f.write("Hello World")
# f.close()
# f.write("Asif")

# f = open('./file-1.txt','w')
# f.write("Hello World")
# f.close()
# f.write("My name is Asif")

#write multiline string
# f = open('./sample1.txt','w')
# f.write("Hello Emon\nThis is file 1")
# f.write('\n')
# f.write("I am 24 years old")
# f.write("\n")
# f.write("Closing file")
# f = open('./file-2.txt','w')
# f.write('Hello World')
# f.write('\n')
# f.write('I am 24 years old')
# f.close()
#if file is already present
# f = open("./sample.txt",'w')
# f.write("Salmon Bhai is my favourite")
# f.close()



#append mode
# f = open('sample1.txt','a')
# f.write("Salmon bhai is my favourite")
# f.close()
# f = open('./sample1.txt','a')
# f.write("\n")
# f.write("Salmon bhai is the don")
# f.close()

# for i in range(1,11):
#   f = open('./sample1.txt','a')
#   f.write(f"Hello {i}\n")
# f.close()

#write many lines
# l = ['Hello\n','i am\n','Asif\n','Arfi\n']
# f = open('./file-2.txt','w')
# f.writelines(l)
# f.close()
# obj1 = 'Hello Python'
# f = open('./file-2.txt','a')
# f.writelines(obj1)
# f.close()

#reading from files - read(),readline()
# f = open('./file-2.txt','r')
# s = f.read()
# print(s)
# f.close()
# f = open('file-2.txt','r')
# print(f.readline())
# print(f.readline())
# s1 =f.readline()
# s2 =f.readline()
# print(s1)
# print(s2)
# f.close()

#reading upto n characters
# f = open('./sample.txt','r')
# print(f.read())
# f = open('./sample1.txt','r')
# print(f.read(20))
# f.close()

print("File handling revise")

#if file is not present
# f = open('sample.txt','w')
# f.write("Hello Asif")
# f.close()
# f.write("I am writing something")

#write multiline strings
# f = open('sample.txt','w')
# f.write("Asif")
# f.write("Emon")
# f.write("\nProbin")
# f.close()

#case-2 : if the file is already present
# f = open('sample.txt','w')
# f.write("Hello Asif")
# f.write("\nI am 24 years old")
# f.close()

# f = open('sample.txt','a')
# f.write('I am appending')
# f.write("How are you?")
# f.close()

print("hi")

# l = ["1","2","3","4","5"]
# t = ('Asif','emon','hasan')
# s = "\nASIF"
# # n = 1231
# f = open('sample.txt','a')
# f.writelines(l)
# f.writelines(t)
# f.writelines(s)
# f.writelines(n)


#reading from files-read/readlines
# f = open('sample.txt','r')
# d = f.read()
# print(d)
# d1 = f.readline()
# d2 = f.readline()
# print(d1,d2)


# f = open('loop.txt','a')
# for i in range(1,11):
#   f.write(f"Hello from {i}\n")
# f.close()

# f = open('loop.txt','r')
# data = f.read()
# print(data)

# f = open('loop.txt','r')
# d1 =f.readline()
# d2 =f.readline()
# d3 =f.readline()
# print(d1)
# print(d2)
# print(d3)

# f = open('loop.txt','r')
# d =f.read(100)
# print(d)

# print("hello")

# f = open('loop.txt','r')
# l1 = f.readline()
# l2 = f.readline()
# print(l1)
# print(l2)

#reading entire file using readline
# f = open('loop.txt','r')
# while True:
#   data = f.readline()
#   if data =='':
#     break
#   else:
#     print(data,end='')

# f.close()

# f = open('file-2.txt','r')
# while True:
#   data = f.readline()
#   if data =='':
#     break
#   else:
#     print(data,end='')
    
# f.close()

# with open('file-2.txt','a') as f:
#   f.write("Salmon bhai")
# f.write("Hello")
# with open('file-2.txt','r') as f:
#   data =f.read()
#   print(data)

# with open('file-2.txt','r') as f:
#   data = f.readline()
#   print(data)
  
