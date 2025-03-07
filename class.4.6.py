def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)
    return transposed

# Input dimensions of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create the matrix
matrix = create_matrix(rows, cols)
print("Original Matrix:")
for row in matrix:
    print(row)

# Transpose the matrix
transposed = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(row)

