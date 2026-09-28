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

        cloned={}
        cloned[node.val]=Node(node.val)
        stack = deque([])
        stack.append(node)
        while stack:
            current = stack.popleft()
            cloned[current.val].neighbors = []
            for neighbor in current.neighbors:
                if neighbor.val not in cloned:
                    cloned[neighbor.val]=Node(neighbor.val)
                    stack.append(neighbor)
                cloned[current.val].neighbors.append(cloned[neighbor.val])
        return cloned[node.val]