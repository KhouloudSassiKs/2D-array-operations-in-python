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

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Traverse an elevation map, always moving to the highest neighboring cell
that is strictly higher than the current altitude.

Args:
    elevation_map (list[list[int]]): 2D grid of elevations.
    start_x (int): Starting row index.
    start_y (int): Starting column index.

Returns:
    list[int]: Sequence of elevations visited along the trek path.
"""
def trek_path(elevation_map: list[list[int]], start_x: int, start_y: int) -> list[int]:
    # Possible moves: East, South, West, North
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    path = [elevation_map[start_x][start_y]]

    while True:
        current_height = path[-1]

        # Find all valid moves to higher neighboring cells
        possible_moves = [
            (start_x + dx, start_y + dy)
            for dx, dy in directions
            if (0 <= start_x + dx < len(elevation_map) and
                0 <= start_y + dy < len(elevation_map[0]) and
                elevation_map[start_x + dx][start_y + dy] > current_height)
        ]

        if not possible_moves:
            break  # No higher neighbors → end trek

        # Pick the neighbor with the highest elevation
        start_x, start_y = max(
            possible_moves,
            key=lambda pos: elevation_map[pos[0]][pos[1]]
        )

        # Add the new elevation to the path
        path.append(elevation_map[start_x][start_y])

    return path


# Example elevation map
mountain = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 5, 6]
    ]

# Starting from (1, 1) → elevation 3
result = trek_path(mountain, 1, 1)
print("Trek path (elevations):", result)
# Output: Trek path (elevations): [3, 5, 6]
