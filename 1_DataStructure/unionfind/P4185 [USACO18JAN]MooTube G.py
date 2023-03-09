n, q = map(int, input().split())
fa = [i for i in range(n+1)]
size = [1 for _ in range(n+1)]

def find(x):
	if fa[x] != x:
		fa[x] = find(fa[x])
	return fa[x]

def union(x, y):
	rx, ry = find(x), find(y)
	fa[ry] = rx
	if rx != ry:
		size[rx] += size[ry]

relation = sorted([tuple(map(int, input().split())) for _ in range(n-1)], key=lambda x: x[2], reverse=True)
ques = [tuple(map(int, input().split())) + (i,) for i in range(q)]

res = [0 for _ in range(q)]
i = 0
for k, v, id_ in sorted(ques, reverse = True):
    while i < n-1:
        p, q, r = relation[i]
        if r >= k:
            union(p, q)
            i += 1
        else: break
    res[id_] = size[find(v)] - 1

print(*res, sep='\n')