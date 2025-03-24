"""
unique binary search tree 의 개수를 리턴
n 개의 노드를 가짐. 1 ~ n 값을 가지는
1 <= n <= 19
결국은 값을 넣는 순서를 찾아야 함

n 개의 노드를 가질 때,
1. tree 의 최대 높이 = n
2. 노드가 들어갈 수 있는 자리 개수 = 1 + 2 + ... + 2^(n-1) = 2^n - 1
3. root 의 값이 k 라면 왼쪽 트리에는 1 ... k-1 까지의 값이 들어가고 (dp[k-1]), 오른쪽 트리에는 k+1 ... n 의 값이 들어감 (dp[n-k])
dp[i] : i 개의 노드로 만들 수 있는 유니크 BST 개수
dp[1] = 1
dp[2] = root == 2 일때, dp[1] + root == 1 일 때, 오른쪽 dp[2-1] = 2
dp[3] = root == 1 dp[0] * dp[2] + root == 2 dp[1] + root == 3 dp[2] = 5`
"""

def solve(n):
    dp = [0 for _ in range(n + 1)]

    dp[0] = 1
    dp[1] = 1

    for k in range(2, n+1):
        dp[k] = 0
        for root in range(1, k+1):
            dp[k] += dp[root-1] * dp[k - root]

    return dp[n]

solve(3)
solve(19)
