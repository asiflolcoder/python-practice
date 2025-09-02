print("Tuple From Tutorialspoint)")
tup1 = (12,32,31,23,11)
tup2 = ("Asif",24,True,3+4j)
print(tup1,type(tup1))
print(tup2,type(tup2))
empty_tup =()
print(empty_tup,type(empty_tup))

tup3 = (23,)
print(tup3,type(tup3))

#accessing tuple values
print(tup1[0],tup1[1])
print(tup2[1:4])

#tuple is immutable - cannot change particular values
tup1 = (1,2,3)
tup2 = ("a","b","c")
# tup1[0] =23
tup3 = tup1 + tup2
print(tup3)
tup4 = tup1[0:2]
print(tup4)

#delete tuple
# del tup1 
# print(tup1)

#tuple concatenation
tup1 = (12,34,22,1)
tup2 = ("abc","cde","efg")
tup3 = tup2 + tup1
print(tup3)

#tuple repitition
tup1 = (12,22,11)
tup2 = tup1 * 4
print(tup2)

print(12 in tup1)
tup4 = ("Abc",)
print(tup4,type(tup4))