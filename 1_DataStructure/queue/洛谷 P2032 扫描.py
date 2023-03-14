from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))
q = deque()

for i in range(n):
	if q and q[0] <= i - k: q.popleft()
	while q and nums[i] > nums[q[-1]]: q.pop()
	q.append(i)
	if i >= k - 1: print(nums[q[0]])