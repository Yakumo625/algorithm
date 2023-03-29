n = int(input())
v = [0, 10, 20, 50, 100]
dp = [1] + [0] * n

for i in range(1, 5):
    for j in range(v[i], n + 1):
        dp[j] += dp[j - v[i]]

print(dp[n])