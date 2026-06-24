class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        # Helper function for recursive DFS backtracking
        # j represents our current character index in word
        def dfs(j, root):
            curr = root
            
            for i in range(j, len(word)):
                char = word[i]
                
                if char == '.':
                    # Wildcard match: try every available path at this level
                    for child in curr.children.values():
                        # If any branch successfully matches the rest of the word, return True
                        if dfs(i + 1, child):
                            return True
                    # If no paths worked, this combination fails
                    return False
                else:
                    # Standard exact match path
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                    
            return curr.is_word

        return dfs(0, self.root)