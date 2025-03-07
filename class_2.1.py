my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

print("Sliced List:", my_list[1:4])

new_list = my_list + [6, 7, 8]
print("Concatenated List:", new_list)

print("Element at index 2:", my_list[2])

my_string = "shivang kandoi"
print("Name:", my_string)

print("Sliced String:", my_string[0:7])

new_string = my_string + " is learning Python"
print("Concatenated String:", new_string)

print("Character at index 3:", my_string[3])

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

print("Sliced Tuple:", my_tuple[1:4])

new_tuple = my_tuple + (6, 7, 8)
print("Concatenated Tuple:", new_tuple)

print("Element at index 2:", my_tuple[2])

my_range = range(1, 6)
print("Range:", list(my_range))

print("Sliced Range:", list(my_range)[1:4])

my_bytearray = bytearray(b'10101')
print("Bytearray:", my_bytearray)

print("Sliced Bytearray:", my_bytearray[1:4])

new_bytearray = my_bytearray + bytearray(b'010')
print("Concatenated Bytearray:", new_bytearray)

print("Element at index 2:", my_bytearray[2])

my_bytes = bytes([1, 0, 1, 0, 1])
print("Bytes:", my_bytes)

print("Sliced Bytes:", my_bytes[1:4])

new_bytes = my_bytes + bytes([0, 1])
print("Concatenated Bytes:", new_bytes)

print("Element at index 2:", my_bytes[2])


str = "welcome to core python\n"
print(str[0])
print(str[3:7])
print(str[11:])
print(str[-1])
print(str*2)