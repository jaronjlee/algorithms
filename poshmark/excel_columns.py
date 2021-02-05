class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = 0

        i = len(s)-1
        power = 0
        while i >= 0:
            letter = s[i]
            value = alpha.index(letter) + 1
            result += value * (26**power)
            power += 1
            i -= 1

        return result
