l, n, k = map(int, input().split())
flags = list(map(int, input().split()))


def check(mid):
	if mid == 0: return False
	cnt = 0
	for i in range(1, n):
		d = flags[i] - flags[i-1]
		cnt += d // mid
		if d % mid == 0: cnt -= 1
	return cnt <= k


i, j = 0, l
while i < j:
	mid = i + j >> 1
	if check(mid): j = mid
	else: i = mid + 1
print(j)