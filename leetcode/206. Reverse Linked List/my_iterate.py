# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        while head != None:
            # record this before losing it
            next_head = head.next

            # reverse the link (from forward to backward)
            head.next = prev_node

            # preparing for next step
            prev_node = head
            head = next_head

        return prev_node
