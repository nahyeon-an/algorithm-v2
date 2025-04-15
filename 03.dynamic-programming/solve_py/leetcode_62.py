def solve(m: int, n: int):
    """
    m * n grid
    robot => top left corner = grid[0][0]
    grid[m-1][n-1] 로 가려고 함
    로봇은 아래 또는 오른쪽으로 갈 수 있음
    도달할 수 있는 possible unique paths 수를 리턴해라
    dp[i][j] : i, j 에 도달하는 거리 가짓수
    = dp[i-1][j] + dp[i][j-1]
    """
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-i][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


solve(3, 7)
solve(3, 2)

