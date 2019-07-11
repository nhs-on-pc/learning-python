"""
b Represents signed integer of size 1 byte
B Represents unsigned integer of size 1 byte
c Represents character of size 1 byte
u Represents unicode character of size 2 bytes
h Represents signed integer of size 2 bytes
H Represents unsigned integer of size 2 bytes
i Represents signed integer of size 2 bytes
I Represents unsigned integer of size 2 bytes
w Represents unicode character of size 4 bytes
l Represents signed integer of size 4 bytes
L Represents unsigned integer of size 4 bytes
f Represents floating point of size 4 bytes
d Represents floating point of size 8 bytes
"""
from array import *
my_array = array('i', [1, 2, 3, 4, 5])

print(my_array[1])
print(my_array[2])
print(my_array[0])
my_array.append(6)
my_array.insert(2, 9)
print(my_array[5])
print(sorted(my_array))

#my_array.append('7')

my_list = [1, 2, 3, 8, 4, 5]
my_list.append(6)
my_list.append('7')
print(my_list)