# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # time: o(n) space:o(n)
        # If the node is empty
        if not root:
            return None
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        # Return the modified root
        return root
