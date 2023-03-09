import sys

sys.setrecursionlimit(114514)


n = int(input())
g = [[c for c in input()] for _ in range(n)]
vis = [[0 for _ in range(n)] for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

island = 0
jud = ans = 0
flag = 1

def dfs(x, y):
	global flag, jud

	vis[x][y] = 1

	flag = 1
	if not jud:
		for xx, yy in [(x + dx, y + dy) for dx, dy in dxy]:
			if g[xx][yy] == '.':
				flag = 0
				break
		if flag: jud = 1

	for dx, dy in dxy:
		xx, yy = x + dx, y + dy
		if xx < 0 or yy < 0 or yy >= n or xx >= n: continue
		if vis[xx][yy]: continue
		if g[xx][yy] != '#': continue
		dfs(xx, yy)

for i in range(n):
	for j in range(n):
		if not vis[i][j] and g[i][j] == '#':
			island += 1
			jud = 0
			dfs(i, j)
			if jud: ans += 1

print(island - ans)

