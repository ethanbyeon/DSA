"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists,
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
    [
        1->4->5,
        1->3->4,
        2->6
    ]
    merging them into one sorted list:
    1->1->2->3->4->4->5->6
"""

from typing import List, Optional


class ListNode(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def merge_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode()
    current = sentinel
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1 is not None:
        current = l1
    elif l2 is not None:
        current = l2
    return sentinel.next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Time Complexity: O(n log k)
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = merge_k_lists(lists[:mid])
    right = merge_k_lists(lists[mid:])
    return merge_lists(left, right)
