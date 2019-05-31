from bigintager import *

a = BigInteger('1241')
b = BigInteger('1233')

# print(a - b)
# print(123 - 22987)
lst = [BigInteger('123'),
       BigInteger('-22987'),
       BigInteger('123'),
       BigInteger('1241'),
       BigInteger('-1233'),
       BigInteger('-1000'),
       BigInteger('999'),
       BigInteger('9'),
       BigInteger('9'),
       BigInteger('0'),
       BigInteger('20'),
       BigInteger('9999999999999'),
       BigInteger('-1000000')
       ]
z = "11111"
y = '1101'
a = z
c = y
print(BigInteger.to_int(a) | BigInteger.to_int(c))
print(int('0b' + a, 2) | int('0b' + c, 2))
# print(bin(56))
# for i in lst:
#     for j in range(1, 200):
#         try:
#             a = str(i // j) != str(int(str(i)) // int(str(j)))
#         except:
#             print(i, j)
