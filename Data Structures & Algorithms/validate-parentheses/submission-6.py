class Solution:
    def isValid(self, s: str) -> bool:
        cases = {']':'[', ')':'(','}':'{'}
        stack = []

        if len(s) == 1:
            return False

        for par in s:
            if par in cases:
                if stack and cases[par] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)
        return len(stack) == 0