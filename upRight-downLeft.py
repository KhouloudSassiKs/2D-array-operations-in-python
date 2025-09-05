"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Traverse a 2D matrix in diagonal zigzag order (top-left to bottom-right).
    
Args:
  matrix (List[List[int]]): 2D list of numbers.
        
Returns:
  List[int]: List of numbers in diagonal zigzag order.
example:
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
 should output: [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
"""
def diagonal_traverse(matrix):
    if not matrix or not matrix[0]:
        return []

    output = []                 # Stores the traversal result
    rows, cols = len(matrix), len(matrix[0])
    row = col = 0               # Starting position
    direction = -1              # -1 = up-right, 1 = down-left

    for _ in range(rows * cols):
        # Append the current element
        output.append(matrix[row][col])

        # Move in the current direction
        if direction == -1:  # Moving up-right
            if col == cols - 1:      # Hit the last column → go down
                row += 1
                direction = 1
            elif row == 0:            # Hit the first row → go right
                col += 1
                direction = 1
            else:                     # Regular up-right move
                row -= 1
                col += 1
        else:  # Moving down-left
            if row == rows - 1:      # Hit the last row → go right
                col += 1
                direction = -1
            elif col == 0:            # Hit the first column → go down
                row += 1
                direction = -1
            else:                     # Regular down-left move
                row += 1
                col -= 1

    return output

bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Print the traversal result
print(diagonal_traverse(bookshelf))
