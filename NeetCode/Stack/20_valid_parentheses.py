"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "(){}[]"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false
"""


def is_valid(s: str) -> bool:
    # Time Complexity: O(n)
    closed_map = {")": "(", "}": "{", "]": "["}
    stack = []
    for open_bracket in s:
        if open_bracket not in closed_map:
            stack.append(open_bracket)
        else:
            top = stack.pop() if stack else ""
            if closed_map[open_bracket] != top:
                return False
    return not stack
