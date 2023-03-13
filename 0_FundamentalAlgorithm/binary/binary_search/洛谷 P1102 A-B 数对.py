# 二分解法 算法复杂度o(nlogn)
n, c = map(int, input().split())
nums = sorted(list(map(int, input().split())))

max_ = nums[-1]
cnt = 0
len_ = len(nums)

for i in range(len_):

	tar = nums[i] + c
	if tar > max_: break

	l, r = 0, len_ - 1
	while l < r:
		mid = l + r >> 1
		if nums[mid] >= tar: r = mid
		else: l = mid + 1
	if nums[r] != tar: continue
	else: ll = r

	l, r = 0, len_ - 1
	while l < r:
		mid = l + r + 1 >> 1
		if nums[mid] <= tar: l = mid
		else: r = mid - 1
	rr = r

	cnt += rr - ll + 1

print(cnt)



# 哈希表 算法复杂度O(n)
# from collections import defaultdict as ddict

# n, c = map(int, input().split())
# nums = list(map(int, input().split()))
# d = ddict(int)

# cnt = 0

# for n in nums:
# 	d[n] += 1

# for n in nums:
# 	tar = n + c
# 	cnt += d[tar]

# print(cnt)



# 双指针 算法复杂度O(nlogn)





