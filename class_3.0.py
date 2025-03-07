import array

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")
print("7. Floor Division")
print("8. Bitwise AND")
print("9. Bitwise OR")
print("10. Bitwise XOR")
print("11. Bitwise NOT")
print("12. Left Shift")
print("13. Right Shift")
print("14. Array Operations")

choice = int(input("Enter your choice (1-14): "))

if choice in range(1, 14):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

if choice == 1:
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
elif choice == 4:
    print(f"Division: {num1} / {num2} = {num1 / num2}")
elif choice == 5:
    print(f"Modulus: {num1} % {num2} = {num1 % num2}")
elif choice == 6:
    print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")
elif choice == 7:
    print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
elif choice == 8:
    print(f"Bitwise AND: {num1} & {num2} = {num1 & num2}")
elif choice == 9:
    print(f"Bitwise OR: {num1} | {num2} = {num1 | num2}")
elif choice == 10:
    print(f"Bitwise XOR: {num1} ^ {num2} = {num1 ^ num2}")
elif choice == 11:
    print(f"Bitwise NOT: ~{num1} = {~num1}")
elif choice == 12:
    print(f"Left Shift: {num1} << {num2} = {num1 << num2}")
elif choice == 13:
    print(f"Right Shift: {num1} >> {num2} = {num1 >> num2}")
elif choice == 14:
    size = int(input("Enter the size of the array: "))
    arr = array.array('i', [])
    print("Enter elements of the array:")
    for i in range(size):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)
    print("Original array:", arr)

    print("Elements in the array:")
    for element in arr:
        print(element, end=' ')
    print()

    new_arr = array.array('i', arr)
    print("New array created from the existing array:", new_arr)
else:
    print("Invalid choice")