# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        carry = 0
        dummy = cur = ListNode() # dummy 用来记住新链表的起点。
        while l1 or l2 or carry:
            if not l1:
                v1 = 0
            else:
                v1 = l1.val
                l1 = l1.next
            if not l2:
                v2 = 0
            else:
                v2 = l2.val
                l2 = l2.next
            
            val = v1 + v2 + carry 
            carry = val // 10 # 整除取进位。比如 15 // 10 = 1
            val = val % 10 # 取余数作为当前位的值。比如 15 % 10 = 5
            cur.next = ListNode(val) # 创建新节点
            cur = cur.next
        return dummy.next

            
                
            
