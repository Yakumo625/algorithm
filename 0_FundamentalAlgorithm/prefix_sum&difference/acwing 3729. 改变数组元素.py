T = int(input())
for _ in range(T):
	n = int(input())
	nums = [0] + list(map(int, input().split()))
	v = [0 for _ in range(n + 2)]

	for i in range(1, n+1):
		if nums[i]:
			if nums[i] > i:
				v[1] += 1
				v[i+1] -= 1
			else:
				v[i - nums[i] + 1] += 1
				v[i+1] -= 1

	for i in range(1, n+1):
		v[i] += v[i-1]
		print(1 if v[i] >= 1 else 0, end=' ')

	print()