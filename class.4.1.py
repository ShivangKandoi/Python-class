# Write a function that takes an array as input and returns the array in reverse order.

def reverse_array(arr):
    return arr[::-1]


arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

reversed_arr = reverse_array(arr)
print("Original array:", arr)
print("Reversed array:", reversed_arr)

