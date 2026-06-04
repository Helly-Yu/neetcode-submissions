# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time: o(n*k) space: o(1)

        if not lists:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i-1], lists[i])
        # # Return the last processed node, which contains everything
        return lists[-1] 
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Set up a dummy node to act as the fixed starting point of the merged list
        # 2. 'curr' is the pointer we use to build and traverse the new list
        curr = dummy = ListNode()

        # 3. Compare nodes only while both a and b are not null 
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1    # Attach node 'a' to the merged list
                list1 = list1.next       # Move pointer 'a' forward
            else:
                curr.next = list2    # Attach node 'b' to the merged list
                list2 = list2.next       # Move pointer 'b' forward
            
            # 4. Move the 'curr' pointer forward to prepare for the next node
            curr = curr.next

        # 5. When the loop ends, at least one list is empty. 
        # Append all remaining nodes of the non-empty list directly.
        curr.next = list1 or list2

        # 6. The actual head of the merged list is the node immediately following the dummy
        return dummy.next