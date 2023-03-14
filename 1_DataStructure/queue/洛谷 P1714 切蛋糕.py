from collections import deque

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

for i in range(1, n+1):
	nums[i] = nums[i] + nums[i-1]

res = nums[1]
q = deque()
for i in range(1, n+1):
	if q and q[0] <= i - (m + 1): q.popleft()
	while q and nums[q[-1]] > nums[i]: q.pop()
	q.append(i)
	if i > 1:
		res = max(res, nums[i] - nums[q[0]])
print(res)