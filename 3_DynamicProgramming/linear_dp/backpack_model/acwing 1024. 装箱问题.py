n, m = map(int, (input(), input()))
v = [0] + [int(input()) for _ in range(m)]
dp = [0] * (n + 1)

for i in range(1, m + 1):
    for j in range(n, v[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - v[i]] + v[i])

print(n - dp[n])