# Write a Programme to get the number of occurrence of specific elements in array

def count_occurrence(arr, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count


arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))

element = int(input("Enter the element to count: "))
occurrences = count_occurrence(arr, element)
print(f"The element {element} occurs {occurrences} times in the array.")