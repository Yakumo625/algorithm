import sys
heap = [0 for _ in range(int(1e6) + 10)]
size = 0

input = lambda: sys.stdin.readline()
write = lambda x: sys.stdout.write(str(x)+'\n')

def up(i):
	while i > 1 and heap[i] < heap[i // 2]:
		heap[i], heap[i // 2] = heap[i // 2], heap[i]
		i >>= 1

def down(i):
	while i * 2 <= size:
		son = i * 2
		if son < size and heap[son+1] < heap[son]: son += 1
		if heap[son] < heap[i]:
			heap[son], heap[i] = heap[i], heap[son]
			i = son
		else: break


n = int(input())
for _ in range(n):
	ops = list(map(int, input().split()))
	op = ops[0]
	if op == 1:
		size += 1
		heap[size] = ops[1]
		up(size)
	elif op == 2:
		write(heap[1])
	else:
		heap[1] = heap[size]
		size -= 1
		down(1)
