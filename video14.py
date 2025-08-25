print("conditional statement")

# marks = 20
# result = ""
# if marks<30:
#   result = "Fail"
# elif marks >75:
#   result = "Passed with distinction"
# else:
#   result = "Passed"

# print(result)

# age = ""
# if age>18:
#   print("He can drive")
# else:
#   print("He cannot drive")

# num = int(input("Enter a number:"))
# if(num<0):
#   print("negative")
# else:
#   print("positive")
  
amount = int(input("Enter amount:"))
dis = 0
if (amount>1000):
  dis = (amount * 10)/100
  amount_to_pay = amount - dis
  print("Payment after discount:",amount_to_pay)
else:
  print("Discount is not available")
  print("Payment is",amount)