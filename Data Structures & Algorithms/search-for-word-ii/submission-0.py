class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word at the leaf node for easy retrieval

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word
            
        rows, cols = len(board), len(board[0])
        res = []

        # 2. Backtracking function
        def dfs(r,c,node):
            char = board[r][c]
            curr_node = node.children[char]
            # If we matched a full word, add it to results
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # Avoid duplicates if the word appears twice
            
            # Mark the cell as visited
            board[r][c] = '#'

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
            
            # Backtrack (restore the cell)
            board[r][c] = char
        
        # 3. Kick off DFS from every cell that matches a Trie root starting character
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return res
            
            