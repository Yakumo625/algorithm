from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
q = deque()

dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs():
	q.append((0, 0))
	d[0][0] = 0
	while q:
		x, y = q.popleft()
		for dx, dy in dxy:
			xx, yy = x + dx, y + dy
			if xx < 0 or yy < 0 or yy >= m or xx >= n: continue
			if d[xx][yy] != -1: continue
			if g[xx][yy] == 1: continue
			q.append((xx, yy))
			d[xx][yy] = d[x][y] + 1
			if (xx, yy) == (n - 1, m - 1): return d[xx][yy]
	return -1

print(bfs())