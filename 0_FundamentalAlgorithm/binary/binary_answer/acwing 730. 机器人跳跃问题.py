n = int(input())
nums = list(map(int, input().split()))

def check(mid):
	s = mid
	for h in nums:
		s = s - (h - s)
	return s >= 0

l, r = 0, max(nums)
while l < r:
	mid = l + r  >> 1
	if check(mid): r = mid
	else: l = mid + 1
print(r)