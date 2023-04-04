import sys
from heapq import *

input = lambda : sys.stdin.readline()
print = lambda x : sys.stdout.write(str(x) + '\n')

n = int(input())
lheap, rheap, mid = [], [], None
for t, num in enumerate(map(int, input().split()), 1):
	if mid is None:
		mid = num
		print(mid)
	else:
		if num > mid: heappush(rheap, num)
		else: heappush(lheap, -num)

		if t & 1:
			l, r = len(lheap), len(rheap)
			if l > r:
				heappush(rheap, mid)
				mid = -heappop(lheap)
			elif l < r:
				heappush(lheap, -mid)
				mid = heappop(rheap)

			print(mid)