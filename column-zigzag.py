 """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Traverses a 2D matrix column by column, moving in a zig-zag up-down.
    starting from the bottom-right, moving upwards, then left, then downwards, etc.

    Args:
        matrix (List[List[int]]): 2D list representing the bookshelf (rows x columns)

    Returns:
        List[int]: List of elements tracing the zig zag steps
    """
def column_traverse(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, cols - 1  # Start from bottom-right corner
    direction = -1  # Start moving upwards
    output = []

    # Loop over all elements in the matrix
    for _ in range(rows * cols):
        output.append(matrix[row][col])  # Add current element to output

        # If moving upwards
        if direction == -1:
            if row == 0:        # Reached top of current column
                direction = 1   # Change direction to downwards
                col -= 1        # Move left to the next column
            else:
                row -= 1        # Continue moving up
        else:  # Moving downwards
            if row == rows - 1:  # Reached bottom of current column
                direction = -1   # Change direction to upwards
                col -= 1         # Move left to the next column
            else:
                row += 1         # Continue moving down             

    return output

# Example matrix resembling a bookshelf (3 shelves, 4 books each)
bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Print the traversal result
print(column_traverse(bookshelf))
