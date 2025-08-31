# Function to check if a neighboring position is empty ('E')
"""
Our target cell is the one at the center [1][1] in the following mini cut
All empty spots on all four directions are candidate for return.
* E *
E E E
* E *
"""
def is_empty_neighbor(board, x, y):
    rows, cols = len(board), len(board[0])
    
    # Ensure coordinates are within the board boundaries
    if 0 <= x < rows and 0 <= y < cols:
        return board[x][y] == 'E'
    return False

def main():
    # Sample board setup
    board = [
        ['P', 'E', 'E', 'P'],
        ['E', 'P', 'E', 'P'],
        ['P', 'E', 'P', 'P'],
        ['P', 'E', 'P', 'E']
    ]
    
    result = []
    rows, cols = len(board), len(board[0])
    
    # Iterate through every cell on the board
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is empty
            if board[i][j] == 'E':
                # Check if any of the four neighbors (up, down, left, right) are empty
                if (
                    is_empty_neighbor(board, i - 1, j) or  # Up
                    is_empty_neighbor(board, i + 1, j) or  # Down
                    is_empty_neighbor(board, i, j - 1) or  # Left
                    is_empty_neighbor(board, i, j + 1)     # Right
                ):
                    result.append((i, j))  # Add position to result if condition is met
    
    print(result)  # Output the list of empty positions with empty neighbors

if __name__ == "__main__":
    main()
