""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Given a grid of altitudes and a starting point, 
return the highest altitude found among the starting cell 
and its immediate North, East, South, and West neighbors.
"""
def find_peak(grid, start_row, start_col):
    rows, cols = len(grid), len(grid[0])
    altitude = grid[start_row][start_col]

    # Check North, East, South, West for higher altitude
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = start_row + dr, start_col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] > altitude:
            altitude = grid[r][c]  # Note: Only checks direct neighbors

    return altitude

# Example mountain terrain grid
mountain = [
     [1, 2, 3],
     [2, 5, 7],
     [4, 6, 9]
    ]

# Starting point: (0, 1) → altitude 2
peak = find_peak(mountain, 0, 1)
print(f"Highest altitude reachable from (0,1) among neighbors: {peak}")
