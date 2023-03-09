from math import sqrt

T = int(input())

def find(x):
	if fa[x] != x:
		fa[x] = find(fa[x])
	return fa[x]

def merge(x, y):
	a, b = find(x), find(y)
	fa[a] = b

def dict(ho1, ho2):
	x1, y1, z1 = ho1
	x2, y2, z2 = ho2
	return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

for _ in range(T):
	n, h, r = map(int, input().split())
	fa = [i for i in range(n)]
	hos = [tuple(map(int, input().split())) for _ in range(n)]

	for i in range(n):
		for j in range(n):
			d = dict(hos[i], hos[j])
			if d <= 2*r: merge(i, j)

	jud, up, down = 0, [], []
	for i in range(n):
		z = hos[i][2]
		if z - r <= 0: down.append(i)
		if z + r >= h: up.append(i)

	for i in up:
		for j in down:
			if find(i) == find(j):
				jud = 1

	print('Yes' if jud else 'No')







			






