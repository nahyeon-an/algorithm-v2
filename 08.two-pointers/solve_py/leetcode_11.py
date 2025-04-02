"""
height 배열 주어짐
n 개의 세로 선 -> (i, 0) ~ (i, height[i]) : i 번째 막대기의 높이가 height[i]
상자를 구성하는 2개의 세로선을 찾아라. 가장 많은 물이 들어가는 상자
그리고 그 상자가 담을 수 있는 최대 물양을 리턴해라
"""
from typing import List


def solve(height: List[int]):
    p1 = 0
    p2 = len(height) - 1
    area = -1

    while p1 < p2:
        h = min(height[p1], height[p2])
        area = max(h * (p2 - p1), area)

        # todo : p1 과 p2 를 이동시키는 조건 ?
        # h[p1], h[p2] 중 더 작은 바를 이동
        if height[p1] > height[p2]:
            p2 = p2 - 1
        else:
            p1 = p1 + 1

    print(area)


solve([1, 8, 6, 2, 5, 4, 8, 3, 7])
solve([1, 1])
solve([1,2,4,3])
