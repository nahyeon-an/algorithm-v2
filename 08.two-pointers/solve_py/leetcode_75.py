"""
Counting Sort
nums 가 주어지는데 원소는 red, white, blue 중 하나임
같은 색이 인접하도록 정렬. in place sort
red : 0
white : 1
blue : 2
nums.length <= 300
라이브러리 sort 함수 사용하지 마라

0, 1, 2 각각이 어디까지 정렬되었는지
"""
from typing import List


def solve(nums: List[int]):
    red = 0
    white = 0
    blue = 0

    for n in nums:
        if n == 0:
            red += 1
        elif n == 1:
            white += 1
        else:
            blue += 1

    # 0 ~ red-1 => 0
    # red ~ red + white-1 => 1
    # red + white ~ red + white + blue -1 => 2

    for i in range(red):
        nums[i] = 0

    for i in range(red, red + white):
        nums[i] = 1

    for i in range(red + white, red + white + blue):
        nums[i] = 2

    print(nums)


solve([2,0,2,1,1,0])
solve([2,0,1])
solve([2,1,0,1])
solve([1,0,2])
