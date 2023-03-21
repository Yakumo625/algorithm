n = int(input())
state = [0 for _ in range(n + 1)]
used = [0 for _ in range(n + 1)]

def dfs(u):
	if u > n:
		for c in state[1:]:
			print(c, end=' ')
		print()
		return

	for i in range(1, n+1):
		if not used[i]: 
			state[u] = i
			used[i] = 1
			dfs(u + 1)
			used[i] = 0

dfs(1)