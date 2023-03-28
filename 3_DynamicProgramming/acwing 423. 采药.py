t, m = map(int, input().split())
v, w = zip((0, 0), *(map(int, input().split()) for _ in range(m)))
dp = [0] * (t + 1)

for i in range(1, m + 1):
    for j in range(t, v[i] - 1, - 1):
        dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        if i == m and j == t: break

print(dp[t])