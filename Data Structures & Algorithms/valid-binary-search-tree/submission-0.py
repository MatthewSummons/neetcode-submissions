# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def in_order(root: Optional[TreeNode]) -> list[int]:
            
            items = []
            if not root:
                return items

            if root.left:
                items.extend(in_order(root.left))
            
            items.append(root.val)
            
            if root.right:
                items.extend(in_order(root.right))
            
            return items
        
        sorted_ = in_order(root)
        for i in range(len(sorted_) - 1):
            if sorted_[i] >= sorted_[i + 1]:
                return False
        return True
            


        