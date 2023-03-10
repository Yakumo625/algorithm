n, m, q = map(int ,input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(n)]
arr[:0] = [[0 for _ in range(m+1)]]

for i in range(1, n+1):
	for j in range(1, m+1):
		arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]

for _ in range(q):
	x1, y1, x2, y2 = map(int ,input().split())
	res = arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1]
	print(res)
