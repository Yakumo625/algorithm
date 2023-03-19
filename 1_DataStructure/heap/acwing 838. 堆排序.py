import sys
input = lambda: sys.stdin.readline()
write = lambda x: sys.stdout.write(str(x) + '\n')

n, m = map(int, input().split())
#根结点如果为零，那么无法满足堆的性质，即2 * i无法找到其子节点
heap = [0] + list(map(int, input().split()))
size = n

def down(i):
	while 2 * i <= size:
		son = 2 * i
		if son < size and heap[son+1] < heap[son]:
			son += 1
		if heap[son] < heap[i]:
			 heap[son], heap[i] = heap[i], heap[son]
			 i = son
		else:
			break

#从i//2开始向后遍历一是为了能够检查所有节点，二是为了由底向上的保持堆的性质，最终才能保证整个堆的性质正确
for i in range(n // 2, 0, -1):
	down(i)

for _ in range(m):
	print(heap[1], end=' ')
	heap[1] = heap[size]
	size -= 1
	down(1)