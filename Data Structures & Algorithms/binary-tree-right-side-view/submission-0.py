# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret = []
        queue = [root]
        while queue:
            node_list = queue 
            queue = []
            ret.append(node_list[0].val)
            for n in node_list:
                if n.right:
                    queue.append(n.right)
                if n.left:
                    queue.append(n.left)
        return ret







