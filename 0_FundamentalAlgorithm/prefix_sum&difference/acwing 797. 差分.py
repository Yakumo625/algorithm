n, m = map(int, input().split())
nums = [0] + list(map(int,input().split())) + [0]
diff = nums[:]

for i in range(1, n+1):
	diff[i] = nums[i] - nums[i-1]

for _ in range(m):
	l, r, c= map(int ,input().split())
	diff[l] += c
	diff[r + 1] -= c

for i in range(1, n+1):
	diff[i] += diff[i-1]
	print(diff[i], end=' ')

