"""
143. Reorder List

You are given the head of a singly linked-list.
The list can be represented as:
    L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes.
Only nodes themselves may be changed.

Example:
    Input: head = [1, 2, 3, 4]
    Output: [1, 4, 2, 3]
"""

from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    # Time Complexity: O(n)
    # Find the middle half
    slow = head
    fast = head.next
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # Reverse the second half
    second = slow.next
    prev = slow.next = None
    while second is not None:
        next = second.next
        second.next = prev
        prev = second
        second = next
    # Merge the two halves
    first = head
    second = prev
    while second is not None:
        next_first = first.next
        next_second = second.next
        first.next = second
        second.next = next_first
        first = next_first
        second = next_second
