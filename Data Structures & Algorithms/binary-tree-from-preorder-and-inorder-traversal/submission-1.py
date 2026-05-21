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
        inorder_map = {val: i for i, val in enumerate(inorder)}
        def dfs(pre_start, in_start, in_end):
            if in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])
            mid = inorder_map[preorder[pre_start]]
            left_size = mid - in_start 
            # inorder [:mid] left subtree [mid + 1:] right subtree
            # preorder [1:mid] , [mid+1:]
            root.left = dfs(pre_start + 1, in_start, mid-1)
            root.right = dfs(pre_start + 1 + left_size, mid+1, in_end)

            return root
        
        return dfs(0,0,len(inorder) - 1)

