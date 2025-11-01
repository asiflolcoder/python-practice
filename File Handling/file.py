#if file is not present
# f = open('./File Handling/sample.txt','w')
# f.write("Hello Asif")
# f.close()
# f.write("I am Asif")

#write multiline string
# f = open('./File Handling/sample1.txt','w')
# f.write("Hi")
# f.write('\nHow are you?')
# f.write("\nI am Asif")
# f.close()

#if file is already present
# f = open('./File Handling/sample.txt','w')
# f.write("Salmon Bhai")
# f.close()

#problem with w mode - replaces the whole file

# f =open('./File Handling/sample.txt','a')
# f.write('\nMy name is Salman Khan\nI am unmarried')
# f.close()

# f = open('./File Handling/sample1.txt','a')
# f.write("\nI am fine")
# f.close()

#writelines
# l = ["\nAsif","\nEmon","\nProbin"]
# f = open('./File Handling/sample2.txt','w')
# f.writelines(l)
# f.close()

# s = "Asif is 24 years old"
# f = open('./File Handling/sample2.txt','a')
# f.writelines(s)
# f.close()

#reading from files