# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: o(n) space: o(1)
        prev, curr = None, head

        while curr:
            temp = curr.next # store the next node
            curr.next = prev # the current node -> Previous node
            prev = curr # Previous node move ahead
            curr = temp # current node move ahead
        return prev
