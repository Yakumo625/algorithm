n, m = map(int, input().split())
fa = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]

def find(x):
	if fa[x] != x: fa[x] = find(fa[x])
	return fa[x]

def merge(x, y):
	a, b = find(x), find(y)
	fa[a] = b
	if a != b:
		size[b] += size[a]

for _ in range(m):
	op, *ab = input().split()
	if op == 'C':
		a, b = map(int, ab)
		merge(a, b)
	elif op == 'Q1':
		a, b = map(int, ab)
		print('Yes' if find(a) == find(b) else 'No')
	else:
		a = int(ab[0])
		print(size[find(a)])