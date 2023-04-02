n = int(input())
pairs = sorted([tuple(map(int, input().split())) for _ in range(n)])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if pairs[i][1] >= pairs[j][1]: dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))