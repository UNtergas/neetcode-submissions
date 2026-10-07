# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            current = stack.pop()
            if not current:
                continue
            current.left, current.right = current.right, current.left
            stack.append(current.left)
            stack.append(current.right)

        return root

