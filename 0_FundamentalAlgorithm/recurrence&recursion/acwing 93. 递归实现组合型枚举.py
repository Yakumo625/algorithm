n, m = map(int, input().split())
state = [0 for _ in range(m+1)]

def dfs(u, s):
	if u > m:
		for c in state[1:]:
			print(c, end=' ')
		print()
		return

	for i in range(s, n + 1):
		state[u] = i
		dfs(u + 1, i + 1)

dfs(1, 1)