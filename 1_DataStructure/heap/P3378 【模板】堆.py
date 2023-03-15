import sys

input = lambda: sys.stdin.readline()
write = lambda x: sys.stdout.write(str(x) + '\n')

n = int(input())
heap = [0 for _ in range(n + 10)]
size = 0

def up(i):
	while i > 1 and heap[i] < heap[i >> 1]:
		heap[i], heap[i >> 1] = heap[i >> 1], heap[i]
		i >>= 1

def down(i):
	while i * 2 <= size:
		son = i * 2
		if son < size and heap[son + 1] < heap[son]: son += 1
		if heap[son] < heap[i]:
			heap[son], heap[i] = heap[i], heap[son]
			i = son
		else: break

for _ in range(n):
	op, *x = map(int, input().split())
	if op == 1:
		size += 1
		heap[size] = x[0]
		up(size)
	elif op == 2:
		write(heap[1])
	elif op == 3:
		heap[1] = heap[size]
		size -= 1
		down(1)