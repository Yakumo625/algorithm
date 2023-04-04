import sys
from heapq import *

input = lambda : sys.stdin.readline()

for _ in range(int(input())):
	idx, n = map(int, input().split())
	print(idx, n + 1 >> 1)

	lheap, rheap, mid, l = [], [], None, 1
	for _ in range(n // 10 + 1):
		for t, num in enumerate(map(int, input().split()), 1):
			if mid is None:
				mid = num
				print(mid, end=' ')
			else:
				if num > mid: heappush(rheap, num)
				else: heappush(lheap, -num)

				if t & 1:
					if len(lheap) > len(rheap):
						heappush(rheap, mid)
						mid = -heappop(lheap)
					elif len(lheap) < len(rheap):
						heappush(lheap, -mid)
						mid = heappop(rheap)
					l += 1
					if l > 10 and l % 10 == 1: print()
					print(mid, end=' ')
	print()
