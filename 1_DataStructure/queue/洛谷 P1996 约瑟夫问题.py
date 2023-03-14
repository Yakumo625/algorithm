# 队列解法
from collections import deque
n, m = map(int, input().split())

q = deque(range(1, n + 1))

cnt = 1
while q:
	if cnt % m == 0: 
		print(q[0], end=' ')
		q.popleft()
	else:
		q.append(q.popleft())
	cnt += 1



# 双链表解法
# n, m = map(int, input().split())
# nums = list(range(1, n+1))

# e = [-1 for _ in range(n + 10)]
# l = [-1 for _ in range(n + 10)]
# r = [-1 for _ in range(n + 10)]

# idx = 0

# def init():
# 	global idx
# 	r[0] = n-1
# 	e[0] = 1
# 	l[n-1] = 0
# 	e[n-1] = n
# 	idx = 1

# def insert(k, x):
# 	global idx
# 	e[idx] = x
# 	l[idx] = k
# 	l[r[k]] = idx
# 	r[idx] = r[k]
# 	r[k] = idx
# 	idx += 1


# def remove(k):
# 	l[r[k]] = l[k]
# 	r[l[k]] = r[k]

# if __name__ == '__main__':

# 	init()

# 	for i in range(1, n-1):
# 		insert(i-1, nums[i])

# 	l[0] = n-1
# 	r[n-1] = 0

# 	i = cnt = out = 0
# 	while out != n-1:
# 		if (cnt+1) % m == 0:
# 			print(e[i], end=' ')
# 			remove(i)
# 			out += 1
# 		cnt += 1
# 		i = r[i]
# 	print(e[i], end='')
