# 手写对顶堆
n = int(input())
nums = list(map(int, input().split()))

lheap, rheap = ([0] * (n + 10) for _ in range(2))
lsize = rsize = 0

def up(i, heap, f):
	while i > 1 and f(heap[i], heap[i >> 1]):
		heap[i], heap[i >> 1] = heap[i >> 1], heap[i]
		i >>= 1

def down(i, heap, size, f):
	while i * 2 <= size:
		son = i * 2
		if son < size and f(heap[son + 1], heap[son]): son += 1
		if f(heap[son], heap[i]):
			heap[son], heap[i] = heap[i], heap[son]
			i = son
		else: break

mid = nums[0]
f1 = lambda x, y: x < y
f2 = lambda x, y: x > y

print(mid)

for i in range(1, n):
	# 如果元素大于mid，放到右边的小根堆中
	if nums[i] > mid:
		rsize += 1
		rheap[rsize] = nums[i]
		up(rsize, rheap, f1)
	else:
	# 否则放到左边的大根堆中
		lsize += 1
		lheap[lsize] = nums[i]
		up(lsize, lheap, f2)

	# 奇数项时调整两边堆的大小，输出中位数
	if (i + 1) % 2 != 0:
		if lsize > rsize:
			# 将mid移到右边的小根堆
			rsize += 1
			rheap[rsize] = mid
			up(rsize, rheap, f1)

			# 将左边大根堆的堆顶值移到mid
			mid = lheap[1]

			# 重新调整大根堆
			lheap[1] = lheap[lsize]
			lsize -= 1
			down(1, lheap, lsize, f2)

		elif lsize < rsize:
			# 将mid移动到左边的大根堆
			lsize += 1
			lheap[lsize] = mid
			up(lsize, lheap, f2)

			# 将右边小根堆的堆顶值移到mid
			mid = rheap[1]

			# 重新调整小根堆
			rheap[1] = rheap[rsize]
			rsize -= 1
			down(1, rheap, rsize, f1)

		# 输出中位数
		print(mid)