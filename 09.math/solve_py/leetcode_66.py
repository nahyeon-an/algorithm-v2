# easy
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 10진수 배열
        # 마지막 자리부터 1을 더함
        # 올림이 발생 X -> 종료
        # 올림이 발생 -> 자릿수 올림
        l = len(digits)
        for i in range(l - 1, -1, -1):
            c = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10

            if c > 0:
                continue
            else:
                break

        if c > 0:
            digits = [1] + digits

        return digits