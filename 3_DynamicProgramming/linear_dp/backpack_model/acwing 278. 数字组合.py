n ,m = map(int ,input().split())
v = [0] + list(map(int, input().split()))
dp = [1] + [0] * m


for i in range(1, n + 1):
    for j in range(m, v[i] - 1, - 1):
        dp[j] += dp[j - v[i]]
        
print(dp[m])