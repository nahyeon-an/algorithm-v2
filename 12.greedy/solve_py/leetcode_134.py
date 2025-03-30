"""
n 개의 gas station
gas[i] : i번째 station 에서 충전할 수 있는 가스량 => circular array
차가 있는데 가스 탱크는 무제한임.
cost[i] : i -> i+1 station 으로 움직이는 비용

0 <= gas.length <= 10^5

가스 스테이션의 시작하는 index 를 리턴해라, if can travel circuit once in the clockwise direction (시계방향으로 한바퀴 돌 수 있는)
else return -1
솔루션이 존재한다면 무조건 1가지 경우뿐임

Hint: if you start from station a and stuck at b, then you can't get to b from any station between a and b.
"""
from typing import List


def solve(gas: List[int], cost: List[int]):
    # gas 총합이 cost 총합보다 작으면 정답은 없음
    if sum(gas) < sum(cost):
        return -1

    tank = 0
    start_index = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            tank = 0
            start_index = i+1

    return start_index


solve([1,2,3,4,5], [3,4,5,1,2])
solve([2,3,4], [3,4,3])
solve([5,1,2,3,4], [4,4,1,5,1])
