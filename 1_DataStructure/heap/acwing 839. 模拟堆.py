N = int(1e5) + 10

heap = [0 for _ in range(N)]
ih = [0 for _ in range(N)]
hi = [0 for _ in range(N)]
size = idx = 0

def swap(i, j):
	ih[hi[i]], ih[hi[j]] = ih[hi[j]], ih[hi[i]]
	hi[i], hi[j] = hi[j], hi[i]
	heap[i], heap[j] = heap[j], heap[i]

def up(i):
	while i > 1 and heap[i] < heap[i >> 1]:
		swap(i, i >> 1)
		i >>= 1

def down(i):
	while i * 2 <= size:
		son = i * 2
		if son < size and heap[son + 1] < heap[son]: son += 1
		if heap[son] < heap[i]:
			swap(son, i)
			i = son
		else: break

for _ in range(int(input())):
	op, *kx = input().split()
	if op == 'I':
		x = int(kx[0])
		size += 1
		idx += 1
		ih[idx], hi[size], heap[size] = size, idx, x
		up(size)
	elif op == 'PM': print(heap[1])
	elif op == 'DM':
		swap(1, size)
		size -= 1
		down(1)
	elif op == 'D':
		kp = ih[int(kx[0])]
		swap(kp, size)
		size -= 1
		up(kp)
		down(kp)
	elif op == 'C':
		kp, x = ih[int(kx[0])], int(kx[1])
		heap[kp] = x
		up(kp)
		down(kp)