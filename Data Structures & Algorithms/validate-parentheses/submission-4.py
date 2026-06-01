class Solution:
    def isValid(self, s: str) -> bool:
        # time: o(n) space: o(n)
        # Early exit for odd-length strings
        if len(s) % 2 != 0:
            return False
        stack = []
        # A dictionary makes the mapping clean and easily expandable
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map:
                top = stack.pop() if stack else '#'

                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0

