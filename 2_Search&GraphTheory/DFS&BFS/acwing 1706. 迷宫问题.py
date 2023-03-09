from collections import deque

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
vis = [[0]*n for _ in range(n)]

dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs():
	q = deque()
	q.append(((0, 0), '0 0\n'))
	vis[0][0] = 1
	while q:
		(x, y), path = q.popleft()
		for xx, yy in [(dx + x, y + dy) for dx, dy in dxy]:
			if xx < 0 or yy < 0 or xx >= n or yy >= n: continue
			if g[xx][yy]: continue
			if vis[xx][yy]: continue

			newpath = path + str(xx) + ' ' + str(yy) + '\n'
			q.append(((xx, yy), newpath))
			vis[xx][yy] = 1

			if (xx, yy) == (n-1, n-1): print(newpath)

bfs()



