class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def same(self, grid, x, y, n):
        for i in range(x, x + n):
            for j in range(y, y + n):
                if grid[x][y] != grid[i][j]:
                    return False                    
        return True
    
    def helper(self, grid, x, y, n):
        #print(grid)
        if self.same(grid, x, y, n):
            node = Node(grid[x][y] == 1, True, None, None, None, None)
        else:
            topLeft = self.helper(grid, x, y, n//2)
            topRight = self.helper(grid, x, y + n//2, n//2)
            bottomLeft = self.helper(grid, x + n//2, y, n//2)
            bottomRight = self.helper(grid, x + n//2, y + n//2, n//2)
            node = Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        return node

    def construct(self, grid: list[list[int]]) -> 'Node':
        return self.helper(grid, 0, 0, len(grid))
