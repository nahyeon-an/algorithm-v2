def climbStairs(n: int) -> int:
    """
    n 개의 계단
    한번에 1 또는 2번의 계단을 오름
    distinct ways 를 구해라

    n = 1
    (1) => 1

    n = 2
    (1, 1), (2) => 2

    n = 3
    (1, 1, 1), (2, 1), (1, 2) => 3

    n = 4
    (1, 1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 2) => 5

    stairs[n] = stairs[n-1] + stairs[n-2]
    """
    stairs = [-1, 1, 2]

    for i in range(3, n + 1):
        stairs.append(stairs[i - 1] + stairs[i - 2])

    return stairs[n]