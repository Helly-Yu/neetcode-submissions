# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time:o(n) space:0(n)
        if root is None:
            return []
        
        res = []
        # initial the queue
        queue = deque([root])

        while queue:
            # the node amount of current layer
            size = len(queue)
            current = []

            for _ in range(size):
                # pop up the most left node
                node = queue.popleft()
                current.append(node.val)
                
                # If it has a left sub node, add it to the queue
                if node.left:
                    queue.append(node.left)
                # same as right side
                if node.right:
                    queue.append(node.right)
                
            # add the current [] to the final result
            res.append(current)
        
        return res
            



            


        

        