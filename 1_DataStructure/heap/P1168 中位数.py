n = int(input())
nums = [0] + list(map(int, input().split()))

def down(u, hp, size, func):
	t = u
	if u * 2 <= size and func(hp[u*2], hp[t]): t = u * 2
	if u * 2 + 1 <= size and func(hp[u*2+1], hp[t]): t = u * 2 + 1
	if t != u:
		hp[t], hp[u] = hp[u], hp[t]
		down(t, hp, size, func)

def up(i, hp, size, func):
	while i > 1 and func(hp[i], hp[i//2]):
		hp[i], hp[i//2] = hp[i//2], hp[i]
		i >>= 1

#定义小根堆和大根堆
shp, lhp = [0 for _ in range(n + 10)], [0 for _ in range(n + 10)]
ssize = lsize = 0

mid = nums[1]
print(mid)
for i in range(2, n+1):

	#大于mid时移入小根堆，反之移到大根堆
	if nums[i] >= mid:
		ssize += 1
		shp[ssize] = nums[i]
		up(ssize, shp, ssize, lambda x, y: x < y)
	else:
		lsize += 1
		lhp[lsize] = nums[i]
		up(lsize, lhp, lsize, lambda x, y: x > y)

	#奇数时输出
	if i % 2:

		if ssize < lsize:
			#mid移到小根堆
			ssize += 1
			shp[ssize] = mid
			up(ssize, shp, ssize, lambda x, y: x < y)

			#mid替换为大根堆堆顶
			mid = lhp[1]

			#大根堆顶出堆顶
			lhp[1] = lhp[lsize]
			lsize -= 1
			down(1, lhp, lsize, lambda x, y: x > y)

		if ssize > lsize:
			#mid移到大根堆
			lsize += 1
			lhp[lsize] = mid
			up(lsize, lhp, lsize, lambda x, y: x > y)

			#mid替换为小根堆堆顶
			mid = shp[1]

			#小根堆顶出堆顶
			shp[1] = shp[ssize]
			ssize -= 1
			down(1, shp, ssize,lambda x, y: x < y)

		print(mid)

		

