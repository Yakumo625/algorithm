n, m = map(int, input().split())
v, w =[0], [0]
dp = [0] * (m + 1)

for _ in range(n):
	vi, wi, s = map(int, input().split())
	k = 1
	while k <= s:
		v.append(vi * k)
		w.append(wi * k)
		s -= k
		k <<= 1
	if s > 0:
		v.append(vi * s)
		w.append(wi * s)

for i in range(1, len(v)):
	for j in range(m + 1):
		dp[j] = max(dp[j], dp[j - v[i]] + w[i])

print(dp[-1])