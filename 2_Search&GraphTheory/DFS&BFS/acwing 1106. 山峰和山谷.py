from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]

dxy = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]

peak = valley = 0

def bfs(x, y):
	global has_higher, has_lower
	q = deque()
	q.append((x, y))
	vis[x][y] = 1
	while q:
		x, y = q.popleft()
		for xx, yy in [(dx + x, dy + y) for dx, dy in dxy]:
			if xx < 0 or yy < 0 or xx >= n or yy >= n: continue
			if g[x][y] != g[xx][yy]:
				if g[x][y] < g[xx][yy]: has_higher = True
				else: has_lower = True
			else:
				if not vis[xx][yy]:
					vis[xx][yy] = 1
					q.append((xx, yy))

for i in range(n):
	for j in range(n):
		if not vis[i][j]:
			has_higher, has_lower = False, False
			bfs(i, j)
			if not has_higher: peak += 1
			if not has_lower: valley += 1

print(peak, valley)











