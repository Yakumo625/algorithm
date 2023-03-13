n, m = map(int, input().split())
nums = list(map(int, input().split()))


def check(mid):
	s = 0
	for num in nums:
		if num > mid: s += num - mid
	return s >= m

l, r = 0, max(nums)
while l < r:
	mid = l + r + 1 >> 1
	if check(mid): l = mid
	else: r = mid - 1
print(r)