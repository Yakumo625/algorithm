from heapq import *

n, m = map(int, input().split())
heap = []

for _ in range(n):
	a, b, c = map(int, input().split())
	f = lambda x, a=a, b=b, c=c: a * x**2 + b * x + c
	for i in range(1, m+1):
		if _ == 0: heappush(heap, -f(i))
		elif f(i) < -heap[0]:
			heappop(heap)
			heappush(heap, -f(i))
		else: break

ans = []
for _ in range(m):
	ans.append(-heappop(heap))
print(*ans[::-1])

'''
=======================================分隔符================================================
'''

# # heapq写法

# from heapq import *

# n, m = map(int, input().split())
# heap = []

# # 由于heapq维护的堆中不能有不可比较对象，因此定义了一个obj类，重载了<和=运算符，这样就可以只比较第一个元素了
# class Obj:
# 	def __init__(self, y, fx):
# 		self.y = y
# 		self.fx = fx

# 	def __lt__(self, other):
# 		return self.y < other.y

# 	def __eq__(self, other):
# 		return self.y == other.y


# for _ in range(n):
# 	a, b, c = map(int, input().split())
# 	f = lambda x, a=a, b=b, c=c: a * x**2 + b * x + c
# 	heappush(heap, Obj(f(1), (f, 1)))


# for _ in range(m):
# 	print(heap[0].y, end=' ')
# 	f, x = heappop(heap).fx
# 	heappush(heap, Obj(f(x+1), (f, x+1)))

'''
=======================================分隔符================================================
'''

# 手写堆
# n, m = map(int, input().split())

# heap = [() for _ in range(m + 10)]
# size = 0

# def up(i):
# 	while i > 1 and heap[i][0] < heap[i >> 1][0]:
# 		heap[i], heap[i >> 1] = heap[i >> 1], heap[i]
# 		i >>= 1

# def down(i):
# 	while i * 2 <= size:
# 		son = i * 2
# 		if son < size and heap[son + 1][0] < heap[son][0]: son += 1
# 		if heap[son][0] < heap[i][0]:
# 			heap[son], heap[i] = heap[i], heap[son]
# 			i = son
# 		else: break

# for _ in range(n):
# 	a, b, c = map(int, input().split())
# 	f = lambda x, a=a, b=b, c=c: a * x**2 + b * x + c

# 	size += 1
# 	heap[size] = (f(1), f, 1)
# 	up(size)

# for _ in range(m):
# 	print(heap[1][0], end=' ')

# 	f, x = heap[1][1:]

# 	heap[1] = heap[size]
# 	size -= 1
# 	down(1)

# 	size += 1
# 	heap[size] = (f(x + 1), f, x + 1)
# 	up(size)
