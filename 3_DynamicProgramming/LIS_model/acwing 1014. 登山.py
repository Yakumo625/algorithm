n = int(input())
nums = list(map(int, input().split()))
dp1, dp2 = [1] * n, [1] * n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]: dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if nums[j] < nums[i]: dp2[i] = max(dp2[i], dp2[j] + 1)

max_len = 0
for i in range(n):
    max_len = max(max_len, dp1[i] + dp2[i] - 1)

print(max_len)