def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    squared_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            squared_matrix[i][j] = matrix[i][j] ** 2

    return squared_matrix

input_matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

input_matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix1 = square_matrix_simple(input_matrix1)
result_matrix2 = square_matrix_simple(input_matrix2)

for row in result_matrix1:
    print(row)
    
print()

for row in result_matrix2:
    print(row)
