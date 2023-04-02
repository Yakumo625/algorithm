# n, m = map(int, input().split())
# v, w = zip((0, 0), *(map(int, input().split()) for _ in range(n)))
# dp = [[0] * (m + 1) for _ in range(n + 1)]

# for i in range(1, n+1):
# 	for j in range(m+1):
# 		dp[i][j] = dp[i-1][j]
# 		if j >= v[i]: dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + w[i])

# print(dp[n][m])


'''
滚动数组优化
'''

n, m = map(int, input().split())
v, w = zip((0, 0), *(map(int, input().split()) for _ in range(n)))
dp = [0 for _ in range(m + 1)]

for i in range(1, n+1):
	for j in range(m, v[i] - 1, -1):
		dp[j] = max(dp[j], dp[j - v[i]] + w[i])

print(dp[-1])