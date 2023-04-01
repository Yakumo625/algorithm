nums = list(map(int, input().split()))
n = len(nums)

f, g = [1] * n, [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] <= nums[j]: f[i] = max(f[i], f[j] + 1)
        if nums[i] > nums[j]: g[i] = max(g[i], g[j] + 1)

print(max(f), max(g), sep='\n')