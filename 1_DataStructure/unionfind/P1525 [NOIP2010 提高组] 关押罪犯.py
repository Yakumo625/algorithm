n, m = map(int, input().split())
hate_pair = sorted([tuple(map(int, input().split())) for _ in range(m)], key=lambda x: x[2], reverse=True)
fa = [i for i in range(n+1)]
d = [0 for i in range(n+1)]

jud = 1

def find(x):
	if fa[x] != x:
		tmp = fa[x]
		fa[x] = find(fa[x])
		d[x] = (d[x] + d[tmp]) % 2
	return fa[x]

for x, y, hate in hate_pair:
	a, b = find(x), find(y)
	if a != b:
		fa[b] = a
		d[b] = (d[x] + d[y] + 1) % 2
	else:
		if d[x] == d[y]:
			print(hate)
			jud = 0
			break

if jud: print(0)