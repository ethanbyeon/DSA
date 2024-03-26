"""
19. Remove Nth Node From End of List

Given the head of a linked list,
remove the nth node from the end of the list and return its head.

Example:
    Input: head = [1, 2, 3, 4, 5], n = 2
    Output: [1, 2, 3, 5]
"""

from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Time Complexity: O(n)
    sentinel = ListNode(0, head)
    left = sentinel
    right = head
    while n > 0 and right is not None:
        right = right.next
        n -= 1
    while right is not None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return sentinel.next
