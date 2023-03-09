from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def bfs(i, j):
	q = deque()
	q.append((i, j))
	vis[i][j] = 1
	while q:
		x, y = q.popleft()
		for xx, yy in [(x + dx, y + dy) for dx, dy in dxy]:
			if xx < 0 or yy < 0 or xx >= n or yy >= n: continue
			if vis[xx][yy]: continue
			if g[xx][yy] == 1: continue
			q.append((xx, yy))
			vis[xx][yy] = 1


for i in range(n):
	for j in range(n):
		if g[i][j] == 0 and not vis[i][j] and(i == 0 or j == 0 or i == n-1  or j == n-1):
			bfs(i, j)

for i in range(n):
	for j in range(n):
		if not vis[i][j] and g[i][j] == 0: print(2, end=' ')
		else: print(g[i][j], end=' ')
	print()