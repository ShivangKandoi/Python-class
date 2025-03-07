def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num = int(input(f"Enter element at position [{i}][{j}]: "))
            row.append(num)
        matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

# Input dimensions of the matrices
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

print("Enter elements for the first matrix:")
matrix1 = input_matrix(rows1, cols1)

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

if cols1 != rows2:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    print("Enter elements for the second matrix:")
    matrix2 = input_matrix(rows2, cols2)

    # Multiply the matrices
    product_matrix = multiply_matrices(matrix1, matrix2)

    # Print the resulting matrix
    print("Product of the matrices:")
    for row in product_matrix:
        print(row)

