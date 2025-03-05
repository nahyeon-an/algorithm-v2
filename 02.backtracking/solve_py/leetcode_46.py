from typing import List


def recursive(nums: List[int], picked: List[int], answer: List[List[int]]):
    if len(nums) == 0:
        answer.append(picked)
        return

    for i, n in enumerate(nums):
        recursive(nums[:i] + nums[i+1:], picked.copy() + [n], answer)


def permute(nums: List[int]) -> List[List[int]]:
    ans = []
    recursive(nums, [], ans)
    return ans


permute([1,2,3])
