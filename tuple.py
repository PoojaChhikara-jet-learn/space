
kids1 = ("Ali", "Sara", "Omar", "Lina", "Zayd")


a, b, c, d, e = kids1
print(kids1[0])

for i in kids1:
    print(i)

print(kids1)
print(kids1[:])
print(kids1[0:])
print(kids1[-5:])

print(kids1[1:4])
print(kids1[1:-1])
print(kids1[-5:-1])



kids2 = ("Maya", "Yusuf", "Noor", "Tariq", "Jana")

m, y, n, t, j = kids2
print(kids2[0])

for i in kids2:
    print(i)

print(kids2)
print(kids2[:])
print(kids2[0:])
print(kids2[-5:])

print(kids2[1:4])
print(kids2[1:-1])
print(kids2[-5:-1])

kids3 = ("Hana", "Zain", "Alya", "Kamil", "Nada")


h, z, al, k, na = kids3
print(kids3[0])

for i in kids3:
    print(i)

print(kids3)
print(kids3[:])
print(kids3[0:])
print(kids3[-5:])

print(kids3[1:4])
print(kids3[1:-1])
print(kids3[-5:-1])


# sets 


sample_list = [1,1,2,2,3,3]

sample_set = set(sample_list)

print(sample_set)

print(sample_set[2])



myset = set([])
myset.add(3)
myset.add(3)
myset.add(2)
myset.add(1)

print(myset)



myset.remove(2)

myset.remove(5)

myset.discard(5)

print(myset)

#Set Operations
# 1) Union
# 2) Intersection
# 3) Difference
# 4) Symmetric Difference



a = {1,2,3,4,5}
b = {4,5,6,7,8}


print(a.union(b))
print(a | b)


print(a.intersection(b))
print(a & b)


print(a.difference(b))
print(a - b)

print(a.symmetric_difference(b))
print(a ^ b)
