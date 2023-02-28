# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:


# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 100
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matrix = [[float('inf')]*(n+1) for _ in range(m+1)]
        matrix[m-1][n] = 0
        matrix[m][n-1] = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                matrix[i][j] = min(matrix[i+1][j],matrix[i][j+1]) + grid[i][j]
        return matrix[0][0]