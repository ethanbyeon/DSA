"""
206. Reverse Linked List

Given the head of a singly linked list,
reverse the list, and return the reversed list.

Example:
    Input: head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
"""


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode | None:
    # Time Complexity: O(n)
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
