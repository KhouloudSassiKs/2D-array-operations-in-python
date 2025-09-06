  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Extracts submatrices from matrix_A and matrix_B based on the given coordinates,
    then interleaves their columns row by row.

    Args:
        matrix_A (list of list of int): First input matrix.
        matrix_B (list of list of int): Second input matrix.
        submatrix_coords (list of tuples): Coordinates for the submatrices.
            Each tuple contains (start_row, end_row, start_col, end_col) in 1-based indexing.

    Returns:
        list of list of int: A new matrix with interleaved columns from the submatrices.

    Example:
        matrix_A = [
            [6, -11, 7, -12],
            [10, -14, 11, -15]
        ]
        matrix_B = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        submatrix_coords = [(1, 2, 1, 2), (1, 2, 3, 4)]

        result = solution(matrix_A, matrix_B, submatrix_coords)
        print(result)
        # Output: [[6, 3, -11, 4], 
                   [10, 7, -14, 8]
                   ]
    """
def solution(matrix_A, matrix_B, submatrix_coords):
    # Unpack submatrix coordinates
    startRowA, endRowA, startColA, endColA = submatrix_coords[0]
    startRowB, endRowB, startColB, endColB = submatrix_coords[1]

    # Extract submatrices (convert 1-based to 0-based indices)
    submatrixA = [row[startColA - 1:endColA] for row in matrix_A[startRowA - 1:endRowA]]
    submatrixB = [row[startColB - 1:endColB] for row in matrix_B[startRowB - 1:endRowB]]

    # Interleave columns row by row
    output = []
    for rowA, rowB in zip(submatrixA, submatrixB):
        combined = []
        for colA, colB in zip(rowA, rowB):
            combined.extend([colA, colB])
        output.append(combined)

    return output


# Example usage
matrix_A = [
     [6, -11, 7, -12],
     [10, -14, 11, -15]
      ]
 matrix_B = [
     [1, 2, 3, 4],
     [5, 6, 7, 8]
      ]
submatrix_coords = [(1, 2, 1, 2), (1, 2, 3, 4)]
result = solution(matrix_A, matrix_B, submatrix_coords)
print(result)
# Output: [[6, 3, -11, 4], [10, 7, -14, 8]]
