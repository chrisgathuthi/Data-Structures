# valid parentheses

"""
Open bracket must be closed by the smae type of brackets
open brackets must be cloded in the correct order.
The stack data structure, opening parentheses must match with the latest parentheses
Time and memory is the O(n)
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"} 
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

s = "()"