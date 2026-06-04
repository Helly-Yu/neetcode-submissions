# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # time: o(n) space:o(1)
        l1, l2 = [], []
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None # Cut the first half off from the second half

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first, second = temp1, temp2
        
        

        

        



