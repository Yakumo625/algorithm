n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

for i in range(1, n+1):
	nums[i] = nums[i] + nums[i-1]

i = j = 1
res = -1
ansl = ansr = None

while j < n:
	while nums[j] - nums[i-1] > m and i < j: i += 1
	if nums[j] - nums[i-1] > res:
		res = nums[j] - nums[i-1]
		ansl, ansr = i, j
	j += 1

print(ansl, ansr, res)
