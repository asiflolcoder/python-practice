def is_even(num):
  """
  This fn return if a given number is odd or even
  input - any valid integer
  output -odd/even
  created on - 3 August 2025
  """
  if type(num) == int:
    if num % 2 ==0:
      return "Even"
    else:
      return "Odd"
  else:
    print("This is not available")

print(is_even("asif"))

# for i in range(1,11):
#   x = is_even(i)
#   print(x)

def power(a=1,b=1):
  return a**b
print(power(2))