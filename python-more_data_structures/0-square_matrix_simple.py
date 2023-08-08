def square_matrix_simple(matrix):
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for element in row:
            if isinstance(element, int):
                squared_row.append(element ** 2)
            else:
                squared_row.append(element)
        squared_matrix.append(squared_row)
    return squared_matrix


new_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = square_matrix_simple(new_matrix)
print(result_matrix)
print(new_matrix)
