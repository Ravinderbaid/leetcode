# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        curr = head
        prev = curr
        while curr:
            if curr.val == val:
                if curr == head:
                    head = curr.next
                    curr = head
                else:
                    prev.next = curr.next
                    if curr:
                        curr = curr.next
            else:
                prev = curr
                if curr:
                    curr = curr.next
        return head
