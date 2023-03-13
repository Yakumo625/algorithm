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


# n, m = map(int, input().split())
# nums = list(map(int ,input().split()))

# i = j = 0
# sum_ = nums[0]
# ansi = ansj = anss = -1

# while j < n:

# 	while sum_ > m and i < j:
# 		sum_ -= nums[i]
# 		i += 1

# 	if sum_ == m:
# 		ansi, ansj, anss = i, j, sum_
# 		break

# 	if sum_ > anss:
# 		ansi, ansj, anss = i, j, sum_

# 	j += 1
# 	if j < n: sum_ += nums[j]

# print(ansi+1, ansj+1, anss)


