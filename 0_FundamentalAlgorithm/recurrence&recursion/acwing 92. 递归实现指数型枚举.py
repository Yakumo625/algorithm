n = int(input())
state = [0 for _ in range(n + 1)]

def dfs(u):
	if u > n:
		for i in range(1, n+1):
			if state[i]: print(i, end=' ')
		print()
		return

	state[u] = 0
	dfs(u + 1)
	state[u] = 1
	dfs(u + 1)

dfs(1)