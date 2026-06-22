# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # time:o(n) space:o(n)
        self.cnt = 0
        self.res = None

        def inorder(node):
            if not node or self.res is not None:
                return
            
            # 1. Visit left subtree
            inorder(node.left)

            # 2. Visit current node
            self.cnt += 1
            if self.cnt == k:
                self.res = node.val
                return
            
            # 3. Visit right subtree
            inorder(node.right)
        
        inorder(root)
        return self.res
        


    
    
        