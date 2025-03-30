"""
nums : 배열. 각 원소는 점프할 수 있는 최대 길이임.
if can reach the last index, return true
else return false

nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from typing import List
from collections import deque


def bfs(nums: List[int]):
    visited = {}
    queue = deque()  # 갈 수 있는 index
    queue.append(0)
    visited[0] = True

    while queue:
        idx = queue.popleft()
        print(f"visit {idx} / {nums[idx]}")

        if idx == len(nums) - 1:
            return True

        max_step = min(idx + nums[idx], len(nums) - 1)
        for next_idx in range(idx + 1, max_step + 1):
            if next_idx not in visited:
                queue.append(next_idx)
                visited[next_idx] = True

    return False


def solve(nums: List[int]):
    farthest = 0  # 가장 멀리 갈 수 있는 곳
    target = len(nums) - 1

    for i in range(len(nums)):
        # i <= farthest 이면 도달 할 수 있음
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])  # 가장 멀리 갈 수 있는 인덱스

        if farthest >= target:
            return True

    return False


solve([2, 3, 1, 1, 4])
solve([3,2,1,0,4])
solve([0,2,3])
solve([1,0,2])
solve([0])