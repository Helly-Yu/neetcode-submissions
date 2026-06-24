# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # time:o(n) space:o(n)
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            
            # left subtree
            left_sum = max(dfs(node.left), 0)
            # right subtree
            right_sum = max(dfs(node.right), 0)
            # left + curr + right
            current_sum = node.val + left_sum + right_sum
            # check if current sum is bigger 
            self.max_sum = max(self.max_sum, current_sum)
            # When returning to the parent node, it only can add one subtree
            return node.val + max(left_sum, right_sum)

        
        dfs(root)
        return self.max_sum