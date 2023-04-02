N, M = map(int, input().split())
k = int(input())
v, m, w = zip((0, 0, 0), *(map(int, input().split()) for _ in range(k)))
dp = [[float('inf')] * (M + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(1, k + 1):
    for j in range(N, -1, -1):
        for k in range(M, -1, -1):
            dp[j][k] = min(dp[j][k], dp[max(0, j - v[i])][max(0, k - m[i])] + w[i])

print(dp[N][M])