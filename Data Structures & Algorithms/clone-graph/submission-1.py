"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cloned = {}
        def dfs(node: Optional['Node'])->Optional['Node']:
            if node.val in cloned:
                return cloned[node.val]
            cloned[node.val]=Node(node.val)
            for n in node.neighbors:
                cloned[node.val].neighbors.append(dfs(n))

            return cloned[node.val]
        
        return dfs(node) 
        # 
