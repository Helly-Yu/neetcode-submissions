class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        start = 0
        end = 0
        # Step 1: Record the last occurrence of each character
        last_occurrence = {char: i for i, char in enumerate(s)}
        # Step 2: Walk through the string
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            # If we reached the furthest point required by all chars in this window
            if i == end:
                result.append(i-start+1)
                start=i + 1 #start the new substring
        return result
