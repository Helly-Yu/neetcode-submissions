# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # time:o(n) space:o(n)
        # Inorder traversal visits the node in the order: Left -> Root -> Right
        # Preorder traversal visits the node in the order: Root -> Left -> Right
        # Level Order Traversal visits all nodes present in the same level completely before visiting the next level
        inorder_map = {val: i for i, val in enumerate(inorder)}
        # Pointer to track the current root in the preorder array
        self.pre_idx = 0

        def dfs(in_left, in_right):
            if in_left > in_right:
                return None
            
            # Select the current root value from preorder and increment the pointer 
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # Find where this root splits the inorder array
            idx = inorder_map[root_val]

            # Build the left and right subtrees
            # Elements to the left of idx in inorder belong to the left subtree
            root.left = dfs(in_left, idx-1)
            # Elements to the right of idx in inorder belong to the right subtree
            root.right = dfs(idx+1, in_right)
            return root
        
        return dfs(0, len(inorder)-1)
