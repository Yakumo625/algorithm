from collections import deque

n =int(input())
g = [[c for c in input()] for _ in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]
q = deque()

island = jud = left = 0

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs(x, y):
	global jud
	vis[x][y] = 1
	q.append((x, y))
	while q:
		x, y = q.popleft()

		if g[x+1][y] == '#' and g[x][y+1] == '#' and g[x-1][y] == '#' and g[x][y-1] == '#':
			jud = 1

		for xx, yy in [(x + dx, y + dy) for dx, dy in dxy]:
			if xx < 0 or yy < 0 or xx >= n or yy >= n: continue
			if g[xx][yy] == '.': continue
			if vis[xx][yy]: continue
			q.append((xx, yy))
			vis[xx][yy] = 1


for i in range(n):
	for j in range(n):
		if not vis[i][j] and g[i][j] == '#':
			island += 1
			jud = 0
			bfs(i, j)
			if jud: left += 1

print(island - left)
