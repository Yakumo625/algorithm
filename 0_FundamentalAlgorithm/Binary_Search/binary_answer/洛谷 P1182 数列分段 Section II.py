n, m = map(int, input().split())
nums = list(map(int, input().split()))

def check(mid):
	s = cnt = 0
	for num in nums:
		if num + s > mid:
			s = num
			cnt += 1
		else:
			s += num
	return cnt + 1 <= m


l, r = max(nums), sum(nums)
while l < r:
	mid = l + r >> 1
	if check(mid): r = mid
	else: l = mid + 1

print(r)