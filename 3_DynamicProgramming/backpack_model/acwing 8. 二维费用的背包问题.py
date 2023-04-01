n, V, M = map(int, input().split())
v, m, w = zip((0, 0, 0), *(map(int, input().split()) for _ in range(n)))
dp = [[0] * (V + 1) for _ in range(M + 1)]

for i in range(1, n):
    for j in range(M, m[i] - 1, -1):
        for k in range(V, v[i] - 1, -1):
            dp[j][k] = max(dp[j][k], dp[j - m[i]][k - v[i]] + w[i])

print(dp[M][V])