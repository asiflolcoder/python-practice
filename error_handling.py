print("Syntax Error")
# print "a"
# print "Hello World"
# marks = 80
# if marks>=80:
# print("A+")
# if True
  # print("Asif")
# fo i in ran(5):
# class A: 

#index error
# l=[1,2,3,4,5]
# print(l[50])
  
#module not found error
# import mata
# print(math.floor(10.4))

#key error
# dict1 ={"name":"Asif"}
# print(dict1["age"])

#typeerror
# print(1 +"a")

#valueerror




#exceptions
# with open('sample.txt','w') as f:
#   f.write("Hello World")
  
# with open('sample.txt','r') as f:
#   print(f.read())

# try:
#   with open('sample1.txt','r') as f:
#     print(f.read())
# except:
#   print("File not found")

try: 
  with open('sample.txt','w') as f:
    f.read()
except:
  print("Operation failed")