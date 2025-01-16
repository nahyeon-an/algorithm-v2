def solve(x: int):
    """
    x = 4 -> 2
    x = 8 -> 2

    x = root(a)
    y <= root(a) < y+1
    y ** 2 <= a < (y+1) ** 2

    y 가 정답
    y = 0 일 때, a = 0
    y = 1 일 때, a = 1, 2, 3
    y = 2 일 때, a = 4, 5, 6, 7, 8
    y = 3 일 때, a = 9, 10, 11, 12, 13, 14, 15

    0 <= x <= 2^31 - 1
    0 <= root(x) <= root(2^31 - 1)

    모든 제곱수를 어떻게 찾지?
    가장 작은 정수부터 하나씩 제곱을 함 -> 그 값이 < x
    """
    y = 0
    sqrt = y * y

    while sqrt <= x:
        y += 1
        sqrt = y * y

    return y - 1