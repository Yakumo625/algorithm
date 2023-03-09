from collections import defaultdict as ddict

n, m = map(int, input().split())
connect = [tuple(map(int, input().split())) for _ in range(m)]
k = int(input())
boom = [int(input()) for _ in range(k)]


fa = [i for i in range(n)]
exist = [1 for _ in range(n)]
for i in boom:
	exist[i] = 0

def find(x):
	if fa[x]!= x:
		fa[x] = find(fa[x])
	return fa[x]

def union(x, y):
	global n_stars
	rx, ry = find(x), find(y)
	if rx != ry:
		fa[ry] = rx
		n_stars -= 1

d = ddict(list)
for x, y in connect:
	if exist[x] and exist[y]:
		union(x, y)
	else:
		d[x].append(y)
		d[y].append(x)

n_stars = 0
for i in range(n):
	if fa[i] == i and exist[i]:
		n_stars += 1

ans = [n_stars]

for i in reversed(boom):
	have_relations = d[i]
	if not have_relations:
		n_stars += 1
		ans.append(n_stars)
	else:
		n_stars += 1
		for j in have_relations:
			if exist[j]: union(i, j)
		ans.append(n_stars)

print(*reversed(ans), sep='\n')

