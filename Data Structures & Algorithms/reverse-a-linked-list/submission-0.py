# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #null->0->1->2->3
        prev, curr = None, head
        # prev = null
        # curr = 0
        while curr:
            temp =curr.next
            # 1. temp = 0 -> 1
            # 2. temp = 1 -> 2
            # 3. temp = 2 -> 3
            # 4. temp = 3 -> null
            curr.next = prev
            print(curr.val)
            # 1. 0 -> null
            # 2. 1 -> 0 -> null
            # 3. 2 -> 1 -> 0 -> null
            # 4. 3 -> 2 -> 1 -> 0 -> null
            prev = curr
            # 1. prev = 0 
            # 2. prev = 1
            # 3. prev = 2
            # 4. prev = 3
            curr = temp
            # 1. curr = 0 -> 1
            # 2. curr = 1 -> 2
            # 3. curr = 2 -> 3
        return prev


