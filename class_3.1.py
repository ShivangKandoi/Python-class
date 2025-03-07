height = int(input("Enter the height of the triangles: "))

print("Right Angle Triangle:")
for i in range(1, height + 1):
    print('*' * i)

print("\nEquilateral Triangle:")
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))