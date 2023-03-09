n, c = map(int, input().split())
fa = [int(input()) for _ in range(n)]
used = [0 for _ in range(n)]

ans = 0

def dfs(s):
	global ans

	if s > c: return 1

	for i in range(n):
		if not used[i]:
			s += fa[i]
			used[i] = 1
			status = dfs(s)
			used[i] = 0
			s -= fa[i]
			if status: break

	ans = max(ans, s)
	return 0

dfs(0)
print(ans)


