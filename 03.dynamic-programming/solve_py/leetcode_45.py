"""
nums.length = n
nums[0] 에서 시작
nums[i] : i 로부터 점프 가능한 최대 길이 -> nums[i+j] 로 점프 가능
- 0 <= j <= nums[i]
- i + j < n

nums[n-1] 에 도달하기 위한 최소한의 점프 횟수를 리턴해라 (모든 테스트 케이스는 항상 도달할 수 있음)

1 <= n <= 10^4 -> n log(n)
0 <= nums[i] <= 1000

"""
from typing import List


def memory_exceeded(nums):
    # dp[i][j] : nums[i] 에서 nums[j] 에 도달하는 최소 횟수
    # 2차원 dp -> memory exceeded
    dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]

    for i in range(len(nums)):
        max_steps = nums[i]

        for j in range(1, max_steps + 1):
            if i + j > len(nums) - 1:
                break
            dp[i][i + j] = 1

        # dp[0][i] 업데이트 필요
        if i == 0:
            continue

        # 이거 이상함
        for k in range(1, i):
            if dp[0][k] > 0 and dp[k][i] > 0:
                if dp[0][i] > 0:
                    dp[0][i] = min(dp[0][k] + dp[k][i], dp[0][i])
                else:
                    dp[0][i] = dp[0][k] + dp[k][i]

    return dp[0][len(nums) - 1]


def jump(nums: List[int]) -> int:
    # dp[i] : nums[i] 에 도달하는 최소 횟수
    dp = [-1 for _ in range(len(nums))]
    dp[0] = 0

    for i in range(len(nums)):
        max_steps = nums[i]

        for j in range(1, max_steps + 1):
            if i + j > len(nums) - 1:
                break

            if dp[i] < 0:
                continue
            elif dp[i + j] < 0:
                dp[i + j] = dp[i] + 1
            else:
                dp[i + j] = min(dp[i] + 1, dp[i + j])

    return dp[len(nums) - 1]


assert jump([2, 3, 1, 1, 4]) == 2
assert jump([2, 3, 0, 1, 4]) == 2
assert jump([1, 1, 1, 1]) == 3
assert jump([0]) == 0
