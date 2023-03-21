n = int(input())
nums = [0] + list(map(int, input().split()))

for i in range(1, n+1):
	nums[i] += nums[i-1]

s, ans, cnt = nums[n], 0, 0

if s % 3 != 0:
	print(0)
	exit()

for i in range(1, n):
	if nums[i] == s // 3 * 2: ans += cnt
	if nums[i] == s // 3: cnt += 1

print(ans)