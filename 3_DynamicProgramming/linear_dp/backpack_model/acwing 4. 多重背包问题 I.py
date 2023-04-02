n, m = map(int, input().split())
v, w, s = zip((0, 0, 0), *(map(int, input().split()) for _ in range(n)))
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        for k in range(s[i] + 1):
            if j < k * v[i]: break
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v[i]] + k * w[i])

print(dp[n][m])