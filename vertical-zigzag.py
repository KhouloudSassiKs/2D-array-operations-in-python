"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Veritcal zigzag Matrix Traversal with Prime Number Extraction

This algo allows to traverse a 2D matrix in a vertical zigzag pattern:
- right
- down
- left
- down
Afterwards we extract all prime numbers encountered during the traversal. 
The `is_prime` function checks if the item is a prime number, and the 
`zigzag_traverse_and_primes` function returns a dictionary mapping the 
position in the traversal to the prime numbers found.

Example:
    matrix = [
        [2, 3, 4],
        [5, 6, 7],
        [8, 9, 10]
    ]
    traverse = [2, 3, 4, 7, 6, 5, 8, 9, 10]
    primes = zigzag_traverse_and_primes(matrix)
    print(primes)  # Output: {0: 2, 1: 3, 3: 5, 5: 7}
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def zigzag_traverse_and_primes(matrix):
    traverse = []
    primes = {}
    rows, cols = len(matrix), len(matrix[0])
    
    direction_right = True
    row = col = 0
    
    for _ in range(rows * cols):
        traverse.append(matrix[row][col])
        
        if direction_right:
            if col == cols - 1:
                direction_right = False
                row += 1
            else:
                col += 1
        else:
            if col == 0:
                direction_right = True
                row += 1
            else:
                col -= 1
    
    for index, value in enumerate(traverse):
        if is_prime(value):
            primes[index] = value
    
    return primes

# Example usage
matrix = [
   [2, 3, 4],
   [5, 6, 7],
   [8, 9, 10]]
print("Primes in traversal:", zigzag_traverse_and_primes(matrix))
