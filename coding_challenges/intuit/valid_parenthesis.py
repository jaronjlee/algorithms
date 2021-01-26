class Solution:
    def isValid(self, s: str) -> bool:
        openB = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for bracket in s:
            if bracket in openB:  # if open bracket
                stack.append(bracket)
            else:  # if closed bracket
                if not stack:
                    return False

                lastOpen = stack.pop(-1)  # last open bracket
                if openB[lastOpen] == bracket:
                    next
                else:
                    return False

        if stack:
            return False
        else:
            return True
