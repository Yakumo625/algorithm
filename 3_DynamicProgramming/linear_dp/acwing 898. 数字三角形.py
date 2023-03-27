n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
dp = nums[-1]

for i in range(n - 2, -1, -1):
	for j in range(len(nums[i])):
		dp[j] = max(dp[j], dp[j + 1]) + nums[i][j]

print(dp[0])