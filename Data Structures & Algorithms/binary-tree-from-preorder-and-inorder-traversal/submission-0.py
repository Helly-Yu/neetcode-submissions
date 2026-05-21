# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Inorder traversal visits the node in the order: Left -> Root -> Right
        # Preorder traversal visits the node in the order: Root -> Left -> Right
        # Level Order Traversal visits all nodes present in the same level completely before visiting the next leve
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # inorder [:mid] left subtree [mid + 1:] right subtree
        # preorder [1:mid] , [mid+1:]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

