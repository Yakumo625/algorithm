# 线段树写法



# 树状数组写法
# import sys

# input = lambda : sys.stdin.readline()
# print = lambda x : sys.stdout.write(str(x) + '\n')

# n, m = map(int, input().split())
# nums = [0] + list(map(int, input().split()))
# tree = [0] * (n + 1)

# lowbit = lambda x: x & -x

# def add(x, k):
# 	while x <= n:
# 		tree[x] += k
# 		x += lowbit(x)

# def query(x):
# 	s = 0
# 	while x > 0:
# 		s += tree[x]
# 		x -= lowbit(x)
# 	return s

# def init():
# 	for i in range(1, n + 1):
# 		add(i, nums[i])

# init()
# for _ in range(m):
# 	op, x, y = map(int, input().split())
# 	if op: add(x, y)
# 	else: print(query(y) - query(x - 1))