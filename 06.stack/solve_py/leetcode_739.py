"""
monotonic stack
기온이 주어짐
answer[i] = i 일에 온도가 올라가기 위해 기다려야 하는 일수. 없다면 0
"""

def solve(temperatures: list[int]):
    n = len(temperatures)
    mono_stack = []
    answers = [0 for _ in range(n)]

    for i in range(n-1, -1, -1):
        while mono_stack and temperatures[mono_stack[-1]] <= temperatures[i]:
            mono_stack.pop()

        if mono_stack:
            answers[i] = mono_stack[-1] - i

        mono_stack.append(i)

    return answers


solve([30, 60, 90])
solve([20, 10, 5, 15])
solve([30, 40, 50, 60])
solve([73, 74, 75, 71, 69, 72, 76, 73])
solve([1, 2, 3])
solve([3, 2, 1])
