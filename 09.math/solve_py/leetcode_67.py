from collections import deque


def addBinary(a: str, b: str) -> str:
    """
    a, b => binary string
    length => 1 ~ 10^4 => nlog(n)
    뒷자리부터 더하다가 carry 발생하면, 앞은 모두 보수 & 맨 앞에 1

    자릿수가 다르면 앞에 0을 채워넣는다
    -> 11 + 01
    뒤에서 부터 더하면서 carry 를 넘겨준다

    1010 + 1011 => 1 0 1 0 1
    """
    if len(a) > len(b):
        # b 에 제로 패딩
        b = "0" * (len(a) - len(b)) + b
    else:
        a = "0" * (len(b) - len(a)) + a

    reverse_a = a[::-1]
    reverse_b = b[::-1]

    q = deque()
    c = 0

    for i in range(len(a)):
        val = (int(reverse_a[i]) + int(reverse_b[i]) + c) % 2
        c = (int(reverse_a[i]) + int(reverse_b[i]) + c) // 2
        q.appendleft(str(val))

    if c > 0:
        q.appendleft(str(c))

    return "".join(q)
