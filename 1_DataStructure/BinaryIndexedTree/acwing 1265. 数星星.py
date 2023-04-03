n, N = int(input()), 32010
tree, res= [0] * N, [0] * n
lowbit = lambda x : x & -x

def add(x, d):
	while x <= N:
		tree[x] += d
		x += lowbit(x)

def query(x):
	s = 0
	while x > 0:
		s += tree[x]
		x -= lowbit(x)
	return s

for _ in range(n):
	x, y = map(int, input().split())
	res[query(x + 1)] += 1
	add(x + 1, 1)

print(*res, sep='\n')