N, M, K = map(int, input().split())
v, m = zip((0, 0), *(map(int, input().split()) for _ in range(K)))
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, K + 1):
    for j in range(N, v[i] - 1, -1):
        for k in range(M - 1, m[i] - 1, -1):
            dp[j][k] = max(dp[j][k], dp[j - v[i]][k - m[i]] + 1)

print(dp[N][M - 1], end = ' ')
k = M - 1
while k > 0 and dp[N][k - 1] == dp[N][M - 1]: k -= 1
print(M - k)