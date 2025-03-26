"""
10진수를 2진수로 변환하기
"""

def solve(n: int) -> int:
    # 10 진수를 2 진수로 변환하기
    q = n
    answer = ""
    cnt = 0

    while q > 0:
        r = q % 2  # remainder
        q = q // 2  # quotient
        answer += str(r)
        cnt += 1

    for _ in range(32 - cnt):
        answer += "0"

    print(answer)
    print(int(answer, 2))
    return int(answer, 2)


solve(0b00000010100101000001111010011100)
