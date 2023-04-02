n, m = map(int, input().split())
dp = [0] * (m + 1)
v, w = [[] for _ in range(110)], [[] for _ in range(110)]

for i in range(1, n + 1):
	nn = int(input())
	for _ in range(nn):
		vii, wii = map(int, input().split())
		v[i].append(vii)
		w[i].append(wii)

for i in range(1, n + 1):
	for j in range(m, -1, -1):
		for k in range(len(v[i])):
			if j >= v[i][k]: dp[j] = max(dp[j], dp[j - v[i][k]] + w[i][k])

print(dp[-1])