def main():
	n, r = map(int, input().split())
	xyw = []
	height = width = 0
	for _ in range(n):
		x, y, w = map(int, input().split())
		height = max(height, x + 1)
		width = max(width, y + 1)
		xyw.append((x, y, w))

	if r >= max(width, height):
		print(sum([w for x, y, w in xyw]))
		return

	arr = [[0] * (width + 2) for _ in range(height + 2)]

	for x, y, w in xyw:
		arr[x + 1][y + 1] += w

	max_ = -1
	for i in range(1, height+1):
		for j in range(1, width+1):
			arr[i][j] += arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1]
			if i >= r and j >= r:
				max_ = max(max_, arr[i][j] - arr[i-r][j] - arr[i][j-r] + arr[i-r][j-r])

	print(max_)

if __name__ == '__main__':
	main()