# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue,ret,leftside = [root], [], True
        while queue:
            next_queue = []
            current_level = [0] * len(queue)
            for i,n in enumerate(queue):
                index = i if leftside else len(queue) - i - 1
                current_level[index] = n.val
                n.left and next_queue.append(n.left)
                n.right and next_queue.append(n.right)

            ret.append(current_level)
            queue = next_queue
            leftside = not leftside
        return ret