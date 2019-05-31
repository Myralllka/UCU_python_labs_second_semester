from polynomial import Polynomial

poly1 = Polynomial()
poly2 = Polynomial()
poly3 = Polynomial()
poly4 = Polynomial()

data_file = open("data1.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly1._append_term(float(degree), float(coefficient))

data_file = open("data2.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly2._append_term(float(degree), float(coefficient))

data_file = open("data3.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly3._append_term(float(degree), float(coefficient))

data_file = open("data4.txt", "r")
data_list = data_file.readlines()
data_file.close()
for line in data_list:
    degree, coefficient = line.strip().split()
    poly4._append_term(float(degree), float(coefficient))


print(poly1)
print(poly2)
print(poly3)
print(poly4)
print(poly1 + poly2)
print(poly1 - poly2)
print(poly1 * poly2)
print(poly4 * poly3)
