def remove_duplicates(arr):
    return list(set(arr))

# Example usage
arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
    
unique_arr = remove_duplicates(arr)
print("Original array:", arr)
print("Array with duplicates removed:", unique_arr)

