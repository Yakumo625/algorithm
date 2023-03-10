n, m = map(int, input().split())
nums = [0] + list(map(int ,input().split()))

for i in range(1, n+1):
	nums[i] = nums[i] + nums[i - 1]

for _ in range(m):
	l, r = map(int ,input().split())
	print(nums[r] - nums[l-1])