def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Matrix is empty")
        return

    max_width = max(len(str(num)) for row in matrix for num in row)

    for row in matrix:
        for num in row:
            print("{:>{width}}".format(num, width=max_width), end=" ")
        print()

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
