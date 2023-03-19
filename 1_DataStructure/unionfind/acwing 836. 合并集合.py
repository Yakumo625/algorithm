n, m = map(int, input().split())
fa = [i for i in range(n+1)]

def find(x):
	if fa[x] != x:
		fa[x] = find(fa[x])
	return fa[x]

def merge(x, y):
	a, b = find(x), find(y)
	fa[a] = b

for _ in range(m):
	op, x, y = list(input().split())
	if op == 'M': merge(*map(int, (x, y)))
	else: print('Yes' if find(int(x)) == find(int(y)) else 'No')