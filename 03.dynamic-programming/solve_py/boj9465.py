"""
https://www.acmicpc.net/problem/9465
스티커 2n 개
2행 n열 배치
뗀 스티커의 왼쪽, 오른쪽, 위, 아래 스티커는 사용할 수 없게 됨

점수의 합이 최대가 되도록 스티커를 떼자
점수의 최댓값을 구하는 프로그램

2n 개의 스티커에서 점수 합이 최대이면서 서로 변을 공유하지 않는 스티커 집합 찾기
변을 공유할 때 두 스티커를 모두 뗄 수는 없음

n : 100,000 -> 10만 ( n log n )

d[i][j] : i행 j번째 칸에서 최대 점수 합 -> 이 식을 세워야 함!!
d[i][j] = max(board[i][j] + dp[i-1][j-1],
            board[i][j] + dp[i][j-2],
            board[i][j] + dp[i-1][j-2] )
"""
import sys

def main():
    # tc 개수
    T = int(sys.stdin.readline())

    for _ in range(T):
        n = int(sys.stdin.readline())
        board = [[], []]
        board[0].extend(map(int, sys.stdin.readline().split()))
        board[1].extend(map(int, sys.stdin.readline().split()))

        dp = [[-1] * n, [-1] * n]
        dp[0][0] = board[0][0]
        dp[1][0] = board[1][0]

        if n > 1:
            dp[0][1] = board[0][1] + dp[1][0]
            dp[1][1] = board[1][1] + dp[0][0]

            for j in range(2, n):
                for i in range(2):
                    dp[i][j] = max(board[i][j] + dp[1-i][j-1], board[i][j] + dp[1-i][j-2], board[i][j] + dp[i][j-2])

        answer = max(dp[0][n-1], dp[1][n-1])
        sys.stdout.write(str(answer) + "\n")


if __name__ == '__main__':
    main()
