from math import floor

n, m, q, u, v, t = map(int, input().split())
heap = [()] + [(i, 0) for i in map(int, input().split())] + [() for _ in range(m+10)]
size = n


def cal(ps, i):
	return heap[ps][0] + (i - heap[ps][1] - 1) * q

def down(u, i):
	t = u
	if u * 2 <= size and cal(u*2, i) > cal(t, i): t = u * 2
	if u * 2 + 1 <= size and cal(u*2+1, i) > cal(t, i): t = u * 2 + 1
	if u != t:
		heap[u], heap[t] = heap[t], heap[u]
		down(t, i)

def up(u, i):
	while u > 1 and cal(u, i) > cal(u//2, i):
		heap[u], heap[u//2] = heap[u//2], heap[u]
		u >>= 1


for i in range(n>>1, 0, -1):
	down(i, 1)

p = u / v

for i in range(1, m+1):

	if i % t == 0: print(int(cal(1, i)), end=' ')

	x = cal(1, i)
	size += 1
	heap[size] = (x - floor(p * x), i)
	up(size, i)

	heap[1] = (floor(p * x), i)
	down(1, i)


print()

for i in range(1, n + m + 1):
	if i % t == 0: print(cal(1, m+1), end=' ')
	heap[1] = heap[size]
	size -= 1
	down(1, m+1)


