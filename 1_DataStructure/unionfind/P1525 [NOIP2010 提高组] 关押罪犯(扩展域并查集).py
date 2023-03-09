n, m = map(int, input().split())
hate_pair = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[2], reverse=True)
fa = [i for i in range(n*2+2)]

def find(x):
	if fa[x] != x:
		fa[x] = find(fa[x])
	return fa[x]

jud = 1

for x, y, hate in hate_pair:
	if find(x) == find(y) or find(x + n) == find(y + n):
		print(hate)
		jud = 0
		break
	else:
		fa[x] = fa[y + n]
		fa[y] = fa[x + n]

if jud: print(0)

