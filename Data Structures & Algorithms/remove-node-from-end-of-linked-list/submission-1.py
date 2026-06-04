# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # time:o(n) space: o(1)
        first = head
        # Use a dummy node to easily handle edge cases
        dumy = second = ListNode(0, head) 

        # Step 1: Move the 'first' pointer 'n' steps ahead to create a gap of 'n'
        while n:
            first = first.next
            n -= 1
        
        # Step 2: Move both pointers together. 
        # When 'first' reaches the end (None), 'second' will be exactly ONE node BEFORE the target node.
        while first:
            first, second = first.next, second.next

        # Step 3: Remove the target node by skipping it in the chain
        second.next = second.next.next

        return dumy.next