# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        result = 0
        while(head):
            result = result*2+head.val
            head = head.next
            n+=1
        return result   
