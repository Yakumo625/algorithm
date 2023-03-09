n, k = map(int, input().split())
fa = [i for i in range(n+1)]
d = [0 for i in range(n+1)]

ans = 0

def find(x):
	if x != fa[x]:
		tmp = fa[x]
		fa[x] = find(fa[x])
		d[x] += d[tmp]
	return fa[x]

def union(x, y, relation):
	global ans
	a, b = find(x), find(y)
	if a != b:
		d[a] = (d[y] - d[x] + relation) % 3
		fa[a] = b
	else:
		if relation != (d[x] - d[y] + 3) % 3: ans += 1

for _ in range(k):
	r, x, y = map(int, input().split())
	if x > n or y > n or (r == 2 and x == y): ans += 1
	else: union(x, y, r-1)

print(ans)