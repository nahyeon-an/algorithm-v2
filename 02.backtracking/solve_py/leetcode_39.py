"""
candidates : distinct integers 로 구성된 배열
합이 target 이 되는 candidates 의 유니크한 조합 리스트를 리턴해라
이 때 한 원소가 여러번(중복으로) 선택될 수 있음
리턴되는 combination 개수는 150 보다 작음

1 <= candidates.length <= 30

brute force ?
"""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    # target 보다 큰 값은 스킵
    results = []

    def recursive(c: List[int], t: int, chosen: List[int]):
        if t == 0:
            return chosen

        for n in c:
            if n > t:
                continue

            # n 보다 작은 숫자는 candidates 에서 빼야함
            if chosen and chosen[-1] > n:
                continue

            result = recursive(c, t - n, chosen + [n])
            if result is not None:
                results.append(result)

    recursive(candidates, target, [])

    return results

combination_sum([2,3,6,7], 7)
combination_sum([2,3,5], 8)
combination_sum([3,5,2], 8)
combination_sum([2], 1)
