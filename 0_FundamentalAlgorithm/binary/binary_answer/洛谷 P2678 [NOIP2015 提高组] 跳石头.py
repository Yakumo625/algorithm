l, n, m = map(int, input().split())
flags = [int(input()) for _ in range(n)] + [l]


def check(mid):
	cnt = 0
	start = 0
	for flag in flags:
		if start + mid > flag:
			cnt += 1
		else:
			start = flag
	return	cnt <= m


l, r = 0, l
while l < r:
	mid = l + r + 1 >> 1
	if check(mid): l = mid
	else: r = mid - 1
print(r)