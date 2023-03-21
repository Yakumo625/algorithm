from collections import defaultdict as ddict

n, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]
d = ddict(int)
d[0] += 1

ans = 0
for i in range(1, n+1):
	nums[i] += nums[i - 1]
	ans += d[nums[i] % k]
	d[nums[i] % k] += 1

print(ans)