n, m = map(int, input().split())

def func(a, b, c, x):
	return a*x**2 + b*x + c

def up(i):
	while i > 1 and heap[i][0] < heap[i//2][0]:
		heap[i], heap[i // 2] = heap[i // 2], heap[i]
		i >>= 1

def down(u):
	t = u
	if u * 2 <= size and heap[u*2][0] < heap[t][0]: t = u * 2
	if u * 2 + 1 <= size and heap[u*2+1][0] < heap[t][0]: t = u * 2 + 1
	if u != t:
		heap[u], heap[t] = heap[t], heap[u]
		down(t)

heap = [() for _ in range(m + 10)]
size = 0

for _ in range(n):
	a, b, c = map(int, input().split())

	y = func(a, b, c, 1)
	size += 1
	heap[size] = (y, a, b, c, 1)
	up(size)

for _ in range(m):
	print(heap[1][0], end=' ')

	a, b, c, p = heap[1][1:]

	heap[1] = heap[size]
	size -= 1
	down(1)

	size += 1
	heap[size] = (func(a, b, c, p+1), a, b, c, p+1)
	up(size)
