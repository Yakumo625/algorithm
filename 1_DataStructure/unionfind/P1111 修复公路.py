n, m = map(int, input().split())
r = sorted([tuple(map(int, input().split())) for _ in range(m)], key = lambda x: x[2])
fa = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]

def find(x):
	if fa[x] != x:
		fa[x] = find(fa[x])
	return fa[x]

def merge(x, y):
	a, b = find(x), find(y)
	fa[a] = b
	if a != b:
		size[b] += size[a]


for x, y, t in r:
	merge(x, y)
	if size[find(x)] == n:
		print(t)
		break

if max(size) != n:
	print(-1)



