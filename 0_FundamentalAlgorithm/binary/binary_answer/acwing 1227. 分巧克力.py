n, k = map(int, input().split())
choco = [tuple(map(int, input().split())) for _ in range(n)]


def check(mid):
	res = 0
	for w, h in choco:
		res += (w // mid) * (h // mid)
	return res >= k

l, r = 1, 100001
while l < r:
	mid = l + r + 1 >> 1
	if check(mid): l = mid
	else: r = mid - 1
print(r)