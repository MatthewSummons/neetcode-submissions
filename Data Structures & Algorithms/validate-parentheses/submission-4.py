class Solution:
    def isValid(self, s: str) -> bool:
        right_to_left = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for brace in s:
            if brace in right_to_left:
                if len(stack) > 0 and stack[-1] == right_to_left[brace]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brace)
        if stack == []:
            return True
        else:
            return False

        