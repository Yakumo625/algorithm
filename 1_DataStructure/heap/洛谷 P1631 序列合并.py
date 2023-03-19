from heapq import *

n = int(input())
a, b = (list(map(int, input().split())) for _ in range(2))
heap = []

for i in range(len(a)):
	for j in range(len(b)):
		s = a[i] + b[j]
		if i == 0: heappush(heap, -s)
		else:
			if s > -heap[0]: break
			else: heapreplace(heap, -s)
			
print(' '.join(map(str, [-heappop(heap) for _ in range(n)][::-1])))