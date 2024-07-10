# easy
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        # n log n 알고리즘
        return len(s.split()[-1])


# 개선
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        # n log n 알고리즘
        s = s.strip()
        l = len(s)

        ans = 0
        for i in range(l - 1, -1, -1):
            if s[i] != ' ':
                ans += 1
            else:
                break
        return ans