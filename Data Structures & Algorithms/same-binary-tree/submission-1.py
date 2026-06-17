# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # time:o(n) space:o(n)
        # Base Case 1: Both nodes are None -> They match perfectly so far
        if not p and not q:
            return True
        # Base Case 2: One is None and the other isn't -> Structural mismatch
        if not p or not q:
            return False
        # Base Case 3: Both exist but have different values -> Value mismatch
        if p.val != q.val:
            return False
        # Recursive Step: The current nodes match, so check both children.
        # Both the left sides AND the right sides must be identical.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

            
            