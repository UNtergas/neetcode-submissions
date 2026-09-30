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

        queue=[root]
        ret=[]
        leftside=False
        while queue: 
            node_list = queue
            queue = []
            current_level = deque([])
            for n in node_list:
                current_level.appendleft(n.val) if leftside else current_level.append(n.val)
                n.left and queue.append(n.left)
                n.right and queue.append(n.right)
            
            leftside = not leftside    
            ret.append(current_level)
        
        return ret


# 

                
            