n = int(input())
arr = [[0] + list(map(int, input().split())) for _ in range(n)]
arr[:0] = [[0] * (n + 1)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 and j == 1: dp[i][j] = arr[i][j]
        else:
            dp[i][j] = float('inf')
            if i > 1: dp[i][j] = min(dp[i][j], dp[i - 1][j] + arr[i][j])
            if j > 1: dp[i][j] = min(dp[i][j], dp[i][j - 1] + arr[i][j])
        print(*dp, sep='\n')
        print()
    print()

print(dp[n][n])