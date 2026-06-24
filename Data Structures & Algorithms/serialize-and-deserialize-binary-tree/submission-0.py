# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # time:o(n) space:o(n)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        def dfs(node):
            if not node:
                self.res.append('N')
                return
            
            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(self.res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = collections.deque(data.split(','))
        print(vals)

        def dfs():
            if not vals:
                return None
            
            val = vals.popleft()

            if val == 'N':
                return None

            node = TreeNode(int(val))       
            node.left = dfs()
            node.right = dfs() 

            return node
        
        return dfs()
