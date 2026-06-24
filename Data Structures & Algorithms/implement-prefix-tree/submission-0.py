class TrieNode:
    def __init__(self):
        # Maps a character to its corresponding child TrieNode.
        # Example: {'a': TrieNode, 'b': TrieNode}
        self.children = {}
        # Flag to indicate whether this node represents the exact end of a complete word.
        self.is_word = False

class PrefixTree:
    def __init__(self):
        # Initialize the root node. The root itself does not store any character.
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the prefix tree.
        """
        curr = self.root
        for char in word:
            # If the character path does not exist, create a new node
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move the pointer to the child node
            curr = curr.children[char]
        
        # After traversing the entire word, mark the final node as a valid word end
        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the prefix tree.
        """
        curr = self.root
        for char in word:
            # If any character in the word path is missing, the word does not exist
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # The path exists, but it's only a complete word if the final node is marked true
        return curr.is_word
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any previously inserted word that has the given prefix.
        """
        curr = self.root
        for char in prefix:
            # If the prefix path breaks at any point, no such prefix exists
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        # Successfully traversed the prefix path, so the prefix must exist
        return True