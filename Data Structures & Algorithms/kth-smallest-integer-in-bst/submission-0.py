# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def in_order(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return []
            
            items = []
            if root.left:
                items.extend(in_order(root.left))
            items.append(root.val)
            if root.right:
                items.extend(in_order(root.right))
            return items
        
        return in_order(root)[k-1]