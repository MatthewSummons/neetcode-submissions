# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans, _ = self.isSubTreeBal(root)
        return ans
    

    def isSubTreeBal(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return True, 0
        
        else:
            l, lh = self.isSubTreeBal(root.left)
            r, rh = self.isSubTreeBal(root.right)

            return (abs(lh - rh) < 2 and l and r, 1 + max(lh, rh))
            
        