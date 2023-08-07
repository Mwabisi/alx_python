def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Matrix is empty")
        return

    for row in matrix:
        row_str = ""
        for i, num in enumerate(row):
            if i == len(row) - 1:
                row_str += str(num) + "$"
            else:
                row_str += str(num) + " "
        print(row_str)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
