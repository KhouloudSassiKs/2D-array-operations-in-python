 """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Swaps two submatrices in a given 2D matrix.

Args:
    matrix (list of list): The input 2D matrix.
    coord_S1 (list/tuple): Coordinates of the first submatrix 
                           [startRow, endRow, startCol, endCol].
    coord_S2 (list/tuple): Coordinates of the second submatrix 
                           [startRow, endRow, startCol, endCol].

    Returns:
        list of list: The matrix with the two submatrices swapped.
"""
def submatrix_swap(matrix, coord_S1, coord_S2):
    # Unpack coordinates for clarity
    startRowA, endRowA, startColA, endColA = coord_S1
    startRowB, endRowB, startColB, endColB = coord_S2

    # Extract the submatrices
    subMatrixA = [row[startColA:endColA] for row in matrix[startRowA:endRowA]]
    subMatrixB = [row[startColB:endColB] for row in matrix[startRowB:endRowB]]

    # Swap the elements
    for i in range(len(subMatrixA)):
        for j in range(len(subMatrixA[0])):
            matrix[startRowA + i][startColA + j] = subMatrixB[i][j]
            matrix[startRowB + i][startColB + j] = subMatrixA[i][j]

    return matrix


# ===================== Example =====================

mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ]

coord1 = [0, 2, 0, 2]  # top-left 2x2 submatrix
coord2 = [2, 4, 2, 4]  # bottom-right 2x2 submatrix

result = submatrix_swap(mat, coord1, coord2)
print("Matrix after swapping submatrices:")
for row in result:
    print(row)
    
# Expected Output:
# [11, 12, 3, 4]
# [15, 16, 7, 8]
# [9, 10, 1, 2]
# [13, 14, 5, 6]
