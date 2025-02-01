"""
run length encoding : 문자열 압축 방법. 연속되는 같은 문자가 등장할 때 (개수 + 값) 으로 나타내는 방법
n -> count and say 의 n 번째 원소를 리턴해라
countAndSay(n) = countAndSay(n-1)의 run length encoding 값

재귀적으로 정의됨 -> advanced : 반복문
"""
def count_and_say(n: int) -> str:
    if n == 1:
        return "1"

    ans = ""
    target = count_and_say(n-1)
    count = 0
    prev = target[0]

    for c in target:
        if c != prev:
            ans += str(count) + prev
            prev = c
            count = 1
        else:
            count += 1

    return ans + str(count) + prev

count_and_say(1)
count_and_say(2)
count_and_say(3)
count_and_say(4)
count_and_say(5)
count_and_say(30)
