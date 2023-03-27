n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    nums[i] += nums[i - 1]

for l in range(2, n + 1):
    for i in range(1, n - l + 2):
        j = i + l - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + nums[j] - nums[i - 1])

print(dp[1][n])