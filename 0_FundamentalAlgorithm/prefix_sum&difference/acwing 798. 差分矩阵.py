n, m, q = map(int ,input().split())
arr = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
arr.append([0] * (m+2))
arr[:0] = [[0] * (m+2)]

diff = [[0] * (m+2) for _ in range(n+2)]



for i in range(1, n+1):
	for j in range(1, m+1):
		diff[i][j] = arr[i][j] - (arr[i-1][j] + arr[i][j-1]) + arr[i-1][j-1]

for _ in range(q):
	x1, y1, x2, y2, c = map(int ,input().split())
	diff[x1][y1] += c
	diff[x1][y2+1] -= c
	diff[x2+1][y1] -= c
	diff[x2+1][y2+1] += c

for i in range(1, n+1):
	for j in range(1, m+1):
		diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
		print(diff[i][j], end=' ')
	print()