# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]
        slow, fast = head, head.next
        
        # when fast reaches the end, the slow one is on the mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge 
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            



        


