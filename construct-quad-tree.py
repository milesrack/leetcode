class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        n = len(grid)
        print(grid)
        val = grid[0][0]
        isLeaf = True
        
        for i in range(n):
            for j in range(len(grid[i])):
                if val != grid[i][j]:
                    isLeaf = False                    
                val = grid[i][j]
                
        if isLeaf:
            node = Node(val, isLeaf, None, None, None, None)
        else:
            # TODO : Subdivide the grids
            topLeft = self.construct(grid[:n//2][:n//2])
            topRight = self.construct(grid[:n//2][n//2:])
            bottomLeft = self.construct(grid[n//2:][:n//2])
            bottomRight = self.construct(grid[n//2:][n//2:])
            node = Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
        return node

s = Solution()
n = s.construct([[0,1],[1,0]])