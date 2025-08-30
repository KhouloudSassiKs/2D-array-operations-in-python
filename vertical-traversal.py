  """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    Traverses a 2D matrix (bookshelves) column by column from right to left,
    starting from the bottom of each column upwards.

    Args:
        matrix (list of lists): 2D list representing rows (shelves) and columns (books)

    Returns:
        list: Elements of the matrix in vertical column-wise order
    """
def vertical_traverse(matrix):
    # Handle empty matrix
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []

    rows, cols = len(matrix), len(matrix[0])

    # Start from bottom-right corner
    row, col = rows - 1, cols - 1
    result = []

    # Loop through each column from rightmost to leftmost
    for book in range(cols - 1, -1, -1):
        # Loop through each shelf from bottom to top in the current column
        for shelf in range(rows - 1, -1, -1):
            result.append(matrix[shelf][book])  # Append the book to the result list

    return result

# Example matrix representing library bookshelves
bookshelves = [
    [21, 22, 23],
    [31, 32, 33],
    [41, 42, 43]
]

# Output the vertical traverse of the bookshelves
print(vertical_traverse(bookshelves))  # [43, 33, 23, 42, 32, 22, 41, 31, 21]
