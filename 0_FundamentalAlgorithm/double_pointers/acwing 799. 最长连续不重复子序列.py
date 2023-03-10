from collections import defaultdict as ddict

n = int(input())
nums = list(map(int ,input().split()))

d = ddict(int)

res = i = 0

for j in range(n):
	d[nums[j]] += 1
	while d[nums[j]] > 1:
		d[nums[i]] -= 1
		i += 1
	res = max(res, j - i + 1)

print(res)