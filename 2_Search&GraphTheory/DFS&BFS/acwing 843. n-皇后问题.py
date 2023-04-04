n = int(input())

g = [['.'] * (n + 1) for _ in range(n + 1)]
col, dg, udg = [0] * n, [0] * 2 * n, [0] * 2 * n

def dfs(u):

	if u == n:
		for r in g: print(*r, sep='')
		print()
		return

	for i in range(n):
		if not col[i] and not dg[n + i - u] and not udg[u + i]:
			g[u][i] = 'g'
			col[i] = dg[n + i - u] = udg[u + i] = 1
			dfs(u + 1)
			g[u][i] = '.'
			col[i] = dg[n + i - u] = udg[u + i] = 0

dfs(0)