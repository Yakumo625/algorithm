n, m = map(int, input().split())
v = [0] + [int(input()) for _ in range(n)]
dp = [1] + [0] * (m + 1)

for i in range(1, n + 1):
    for j in range(v[i], m + 1):
        dp[j] += dp[j - v[i]]

print(dp[m])