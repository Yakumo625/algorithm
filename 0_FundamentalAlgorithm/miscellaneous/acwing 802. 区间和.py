n, m = map(int, input().split())
adds = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

#将要处理元素的下标的绝对位置调整为相对位置
positions = [add[0] for add in adds] + [i for query in queries for i in query]
positions = sorted(set(positions))

#建立下标映射, 由于后面要前缀和处理，因此映射下标要+1
d = {positions[i]: i + 1 for i in range(len(positions))}

#根据相对位置重新构建数组
nums = [0 for _ in range(len(positions) + 1)]
for add in adds:
	x, c = add
	nums[d[x]] += c

#前缀和处理
for i in range(1, len(nums)):
	nums[i] += nums[i-1]

#打印结果
for query in queries:
	l, r = map(lambda x: d[x], query)
	print(nums[r] - nums[l-1])
