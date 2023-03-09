from collections import deque

n, m = map(int, input().split())
g = [[c for c in input()] for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def bfs(x, y):
	q = deque()
	q.append((x, y))
	vis[x][y] = 1

	while q:
		x, y = q.popleft()
		for xx, yy in [(dx + x, dy + y) for dx, dy in dxy]:
			if xx < 0 or yy < 0 or xx >= n or yy >= m: continue
			if vis[xx][yy]: continue
			if g[xx][yy] == '.': continue

			q.append((xx, yy))
			vis[xx][yy] = 1


ans = 0
for i in range(n):
	for j in range(m):
		if not vis[i][j] and g[i][j] == 'W':
			ans += 1
			bfs(i, j)

print(ans)
