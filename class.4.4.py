import numpy as np

# Get the size of the array from the user
size = int(input("Enter the size of the array: "))

# Create an array using the numpy array function
array_from_list = np.array([i for i in range(size)])
print("Array from list:", array_from_list)

# Create an array using the numpy linspace function
linspace_array = np.linspace(0, 1, num=size)
print("Linspace array:", linspace_array)

# Create an array using the numpy arange function
start = float(input("Enter the start of the range: "))
end = float(input("Enter the end of the range: "))
step = float(input("Enter the step of the range: "))
arange_array = np.arange(start, end, step)
print("Arange array:", arange_array)

