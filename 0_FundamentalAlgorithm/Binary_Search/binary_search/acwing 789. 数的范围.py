n, q = map(int ,input().split())
nums = list(map(int, input().split()))

for _ in range(q):
	tar = int(input())
	l, r = 0, n-1
	while l < r:
		mid = l + r >> 1
		if nums[mid] >= tar: r = mid
		else: l = mid + 1
	if nums[r] == tar: print(r, end=' ')
	else: print(-1, end=' ')

	l, r = 0, n-1
	while l < r:
		mid = l + r + 1 >> 1
		if nums[mid] <= tar: l = mid
		else: r = mid -1
	if nums[r] == tar: print(r)
	else: print(-1)