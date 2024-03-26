"""
206. Reverse Linked List

Given the head of a singly linked list,
reverse the list, and return the reversed list.

Example:
    Input: head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
"""

from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # Time Complexity: O(n)
    # Recursive Approach:
    # if head is None:
    #     return None
    # new_head = head
    # if head.next is not None:
    #     new_head = reverse_list(head.next)
    #     head.next.next = head
    # head.next = None
    # return new_head
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
