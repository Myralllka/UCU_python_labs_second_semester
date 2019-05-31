from multiset.multisetll import *

a = Multiset()

for i in range(10):
    a.add(i)
print(a)
a1 = a.split_half()

print(a1[0], '\n', a1[1], sep='')

a2 = a.remove_all()
print(a2)
