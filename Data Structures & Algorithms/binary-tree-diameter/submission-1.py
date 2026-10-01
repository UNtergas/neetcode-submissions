# Definitionora binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0
        resultbox={}
        stack=[(root,False)]
        while stack:
            node, ready = stack.pop()
            if not ready:
                stack.append((node,True))
                if node.right: stack.append((node.right,False))
                if node.left: stack.append((node.left,False))
            else:
                left=resultbox.get(node.left,0)
                right=resultbox.get(node.right,0)
                best=max(best,left+right)
                resultbox[node]=1+max(left,right)
        return best
        
        





                