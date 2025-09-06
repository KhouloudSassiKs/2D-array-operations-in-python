"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Extracts the first 'n' boundary layers from matrix_A and matrix_B,
merges them into a single array, and returns the combined result.

Args:
    matrix_A (list of list of int): First input matrix
    matrix_B (list of list of int): Second input matrix
    n (int): Number of outer layers to extract

Returns:
    list: Combined array of elements from the first 'n' layers of both matrices
"""
def solution(matrix_A, matrix_B, n):
    peelingA = []
    peelingB = []

    for i in range(n):
        # Extract the i-th inner submatrix by trimming 'i' rows and columns from each side
        submatrixA = [row[i:len(matrix_A[0]) - i] for row in matrix_A[i:len(matrix_A) - i]]
        submatrixB = [row[i:len(matrix_B[0]) - i] for row in matrix_B[i:len(matrix_B) - i]]

        # Get the outer layer of the submatrix and append to the peeling list
        peelingA.extend(getLayer(submatrixA))
        peelingB.extend(getLayer(submatrixB))

    # Merge the layers from both matrices
    return peelingA + peelingB

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Returns the outermost layer of a 2D matrix in clockwise order.

Args:
    matrix (list of list of int): Input submatrix

Returns:
    list: Elements of the outer layer in clockwise order
"""
def getLayer(matrix):
    layer = []
    rows, cols = len(matrix), len(matrix[0])

    # Define the boundaries of the matrix
    startRow, startCol, endRow, endCol = 0, 0, rows - 1, cols - 1

    # Top row (left to right)
    layer.extend(matrix[startRow][startCol:endCol + 1])

    # Right column, bottom row, and left column if the matrix has more than one row
    if rows > 1:
        # Right column (top to bottom, excluding corners)
        for r in range(startRow + 1, endRow):
            layer.append(matrix[r][endCol])

        # Bottom row (right to left)
        layer.extend(matrix[endRow][startCol:endCol + 1][::-1])

        # Left column (bottom to top, excluding corners)
        for r in range(endRow - 1, startRow, -1):
            layer.append(matrix[r][startCol])

    return layer
# ===================== EXAMPLES =====================

# Example 1: n = 1, 4x4 matrices
matrix_A1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ]
matrix_B1 = [
        [101,102,103,104],
        [105,106,107,108],
        [109,110,111,112],
        [113,114,115,116]
    ]
n1 = 1
result1 = solution(matrix_A1, matrix_B1, n1)
print("Example 1 - n=1, 4x4 matrices:")
print(result1)
# Expected output:
# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5,
#  101, 102, 103, 104, 108, 112, 116, 115, 114, 113, 109, 105]
print()

# Example 2: n = 2, 4x4 matrices
n2 = 2
result2 = solution(matrix_A1, matrix_B1, n2)
print("Example 2 - n=2, 4x4 matrices:")
print(result2)
# Expected output:
# Outer layer + inner layer from A:
# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
# Outer layer + inner layer from B:
# [101, 102, 103, 104, 108, 112, 116, 115, 114, 113, 109, 105, 106, 107, 111, 110]
# Combined:
# [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10,
#  101, 102, 103, 104, 108, 112, 116, 115, 114, 113, 109, 105, 106, 107, 111, 110]
print()

# Example 3: n = 1, 1x1 matrices
matrix_A3 = [[42]]
matrix_B3 = [[99]]
n3 = 1
result3 = solution(matrix_A3, matrix_B3, n3)
print("Example 3 - n=1, 1x1 matrices:")
print(result3)
# Expected output: [42, 99]
