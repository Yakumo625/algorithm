from collections import deque

m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
vis = [[0 for _ in range(n)] for _ in range(m)]

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]


def bfs(x, y):
	q = deque()
	q.append((x, y))
	area = 1
	vis[x][y] = 1
	while q:
		x, y = q.popleft()
		for i in range(4):
			if (g[x][y] >> i & 1): continue
			xx, yy = x + dx[i], y + dy[i]
			if xx < 0 or yy < 0 or xx >= m or yy >= n: continue
			if vis[xx][yy]: continue

			q.append((xx, yy))
			vis[xx][yy] = 1
			area += 1
	return area



ans = max_ = 0
for i in range(m):
	for j in range(n):
		if not vis[i][j]:
			ans += 1
			max_ = max(max_, bfs(i, j))

print(ans, max_, sep='\n')
