# Function to input a matrix
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Input dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements for the first matrix:")
matrix1 = input_matrix(rows, cols)

print("Enter elements for the second matrix:")
matrix2 = input_matrix(rows, cols)

# Add the matrices
sum_matrix = add_matrices(matrix1, matrix2)

# Print the resulting matrix
print("Sum of the matrices:")
for row in sum_matrix:
    print(row)

