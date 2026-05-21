# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head 
        dumy = second = ListNode(0, head) # ListNode(0, head) 创建了一个新节点，它的 next 指向当前的 head
        while n:
            first = first.next
            n-=1
        
        while first:
            first = first.next
            second = second.next

        
        second.next = second.next.next # 你需要站在“待删除节点”的前一个位置，然后执行 prev.next = prev.next.next。
        return dumy.next
        

        



        
