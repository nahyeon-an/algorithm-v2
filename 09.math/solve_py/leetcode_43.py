"""
num1 * num2 를 string 으로 리턴해라
- int 로 변환하는 built in 사용 금지

num1.length, num2.length => 1 ~ 200
"""
def multiply(num1: str, num2: str):

    ans = 0

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            a = ord(num1[i]) - ord('0')
            b = ord(num2[j]) - ord('0')
            ans += a * b * (10 ** (len(num2) - 1 - j + len(num1) - 1 - i))

    return str(ans)


multiply("2", "3")
multiply("20", "31")