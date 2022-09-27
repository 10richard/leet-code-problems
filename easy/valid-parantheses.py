class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
        "}": "{",
        ")": "(",
        "]": "["
        }

        stack = []

        for close in s:
            if close in bracketMap:
                if stack and stack[-1] == bracketMap[close]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(close)
                
        return True if not stack else False