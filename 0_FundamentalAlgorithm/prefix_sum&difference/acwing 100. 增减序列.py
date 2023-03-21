n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
diff = [0 for _ in range(n + 2)]

p = q = 0
for i in range(1, n+1):
	diff[i] = nums[i] - nums[i-1]
	if  i > 1 and diff[i] > 0: p += diff[i]
	elif i > 1 and diff[i] < 0: q -= diff[i]

print(max(p, q))
print(abs(p - q) + 1)