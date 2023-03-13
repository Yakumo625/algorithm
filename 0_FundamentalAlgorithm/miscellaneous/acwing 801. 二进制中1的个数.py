n = int(input())
nums = list(map(int, input().split()))

for i in nums:
	cnt = 0
	while i > 0:
		i -= i & -i
		cnt += 1
	print(cnt, end = ' ')





# n = int(input())
# nums = list(map(int, input().split()))

# for i in nums:
# 	cnt = 0
# 	while i > 0:
# 		cnt += i & 1
# 		i >>= 1
# 	print(cnt, end=' ')
