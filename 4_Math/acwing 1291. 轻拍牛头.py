from collections import defaultdict as ddict

n = int(input())
nums = [int(input()) for _ in range(n)]
cnt, res = ddict(int), ddict(int)

for num in nums:
    cnt[num] += 1

seq = sorted(set(nums))
for i in seq:
    for j in range(1, seq[-1] // i + 1):
        if j * i not in cnt: continue
        res[j * i] += cnt[i]

for num in nums:
    print(res[num] - 1)