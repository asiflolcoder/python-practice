#extract digits from a number
n = 7890
res =[]
count =0
while n!=0:
  dig = n %10
  count = count + 1
  res.append(dig)
  n = n//10

res.reverse()
print(res)
print("Digits:",count)