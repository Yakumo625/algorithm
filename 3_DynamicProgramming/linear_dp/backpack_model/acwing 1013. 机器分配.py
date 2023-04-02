n, m = map(int ,input().split())
w = [[0] + list(map(int, input().split())) for _ in range(n)]
w[:0] = [[0] * (m + 1)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(m + 1):
        for k in range(j + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + w[i][k])

print(dp[n][m])

anss, j = [], m
for i in range(n, 0, -1):
    for k in range(m + 1):
        if dp[i][j] == dp[i - 1][j - k] + w[i][k]:
            anss.append((i, k))
            j -= k
            break
        
for ans in anss[::-1]: print(*ans)