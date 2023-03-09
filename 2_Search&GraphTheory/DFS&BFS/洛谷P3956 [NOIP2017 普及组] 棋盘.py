from collections import deque

m, n = map(int, input().split())
g = [[-1 for _ in range(m)] for _ in range(m)]
for _ in range(n):
	x, y, c = map(int, input().split())
	g[x-1][y-1] = c
vis = [[0 for _ in range(m)] for _ in range(m)]
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

ans = 1145141919

def bfs():
	global ans
	q = deque()
	q.append((0, 0, 0))
	vis[0][0] = 1
	while q:
		x, y, v = q.popleft()
		for xx, yy in [(x + dx, y + dy) for dx, dy in dxy]:
			#越界
			if xx < 0 or yy < 0 or xx >= m or yy >= m: continue
			#访问过
			if vis[xx][yy] == 1: continue
			#无色块遇到无色块
			if g[x][y] == -1 and g[xx][yy] == -1: continue

			vis[xx][yy] = 1
			#相同色块相遇 和 无色块遇到有色块 加0，故无需特判
			vv  = v + 0
			#有色块遇到无色块
			if g[xx][yy] == -1: vv = v + 2
			#不同色块相遇
			elif g[x][y] != -1 and g[xx][yy] != g[x][y]: vv = v + 1
		
			q.append((xx, yy, vv))

			if (xx, yy) == (m-1, m-1):
				ans = min(ans, vv)

bfs()
print(ans if ans != 1145141919 else -1)












