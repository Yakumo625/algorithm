from collections import deque
n, m, x, y = map(int, input().split())
dis = [[-1 for _ in range(m)] for _ in range(n)]
dxy = [(-1, -2), (1, -2), (-1, 2), (1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1)]

def bfs(i, j):
	q = deque()
	q.append((i, j))
	dis[i][j] = 0
	while q:
		x, y = q.popleft()
		for xx, yy in [(x + dx, y + dy) for dx, dy in dxy]:
			if xx < 0 or yy < 0 or xx >= n or yy >= m: continue
			if dis[xx][yy] != -1: continue
			q.append((xx, yy))
			dis[xx][yy] = dis[x][y] + 1

bfs(x-1, y-1)
for d in dis:
	print(*d)


