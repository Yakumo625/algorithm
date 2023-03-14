n, k = map(int, input().split())
nums = list(map(int, input().split()))

from collections import deque

def func(f):
	q = deque()
	for i in range(n):
		while q and q[0] <= i - k: q.popleft()
		while q and f(nums[q[-1]], nums[i]): q.pop()
		q.append(i)
		if i >= k - 1: print(nums[q[0]], end=' ')
	print()

func(lambda x, y: x > y)
func(lambda x, y: x < y)