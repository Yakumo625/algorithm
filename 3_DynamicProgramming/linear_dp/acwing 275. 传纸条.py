m, n = map(int, input().split())
w = [[0] + list(map(int, input().split())) for _ in range(m)]
w[:0] = [[0] * (n + 1)]

dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(n + m + 1)]

for k in range(2, m + n + 1):
    for i1 in range(1, m + 1):
        for i2 in range(1, m + 1):
            j1, j2 = k - i1, k - i2
            if j1 >= 1 and j1 <= n and j2 >= 1 and j2 <= n:
                t = w[i1][j1]
                if i1 != i2: t += w[i2][j2]
                dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1 - 1][i2 - 1] + t)
                dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1][i2 - 1] + t)
                dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1 - 1][i2] + t)
                dp[k][i1][i2] = max(dp[k][i1][i2], dp[k - 1][i1][i2] + t)

print(dp[n + m][m][m])