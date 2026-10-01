# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        resultbox={}
        stack=[(root,False)]
        while stack:
            node,ready = stack.pop()
            if node.val == p.val or node.val == q.val:
                resultbox[node] = node
                continue
            if not ready:
                stack.append((node,True))
                if node.right: stack.append((node.right, False))
                if node.left: stack.append((node.left, False))
            else:
                # check the mailbox
                left = resultbox.get(node.left)
                right = resultbox.get(node.right)

                # meaning find both p and q here
                if left and right:
                    resultbox[node]=node
                else:
                    resultbox[node] = left or right

        return resultbox[root]

                    

            