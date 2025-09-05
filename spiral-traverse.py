"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Traverse a 2D grid in spiral order and return the indices of vowels
encountered in that traversal.

Args:
    grid (List[List[str]]): 2D list of characters.

Returns:
    List[int]: Indices of vowels in the spiral traversal order.
"""
def spiral_traverse_and_vowels(grid):
    if not grid or not grid[0]:
        return []

    traverse = []  # Stores the elements in spiral order
    output = []    # Stores indices of vowels in traverse

    rows, cols = len(grid), len(grid[0])
    startRow, endRow = 0, rows - 1
    startCol, endCol = 0, cols - 1

    # Direction constants
    RIGHT, DOWN, LEFT, UP = 1, 2, 3, 4
    direction = RIGHT

    row = col = 0  # Starting position

    # Traverse all cells
    for _ in range(rows * cols):
        traverse.append(grid[row][col])

        if direction == RIGHT:
            if col == endCol:       # Hit the right boundary
                direction = DOWN
                startRow += 1
                row += 1
            else:
                col += 1
        elif direction == DOWN:
            if row == endRow:       # Hit the bottom boundary
                direction = LEFT
                endCol -= 1
                col -= 1
            else:
                row += 1
        elif direction == LEFT:
            if col == startCol:     # Hit the left boundary
                direction = UP
                endRow -= 1
                row -= 1
            else:
                col -= 1
        else:  # UP
            if row == startRow:     # Hit the top boundary
                direction = RIGHT
                startCol += 1
                col += 1
            else:
                row -= 1

    # Keep the last loop exactly like your original
    for i in range(len(traverse)):
        if traverse[i] in "aeiou":
            output.append(i)

    return output
# Example 1: Multiple rows and columns
grid1 = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]
print("Example 1:", spiral_traverse_and_vowels(grid1))  # Output: [0, 4, 8]

# Example 2: Single row
grid2 = [["a", "b", "c", "d", "e"]]
print("Example 2:", spiral_traverse_and_vowels(grid2))  # Output: [0, 4]

# Example 3: Single column
grid3 = [
    ["a"],
    ["b"],
    ["c"],
    ["d"]
]
print("Example 3:", spiral_traverse_and_vowels(grid3))  # Output: [0]
