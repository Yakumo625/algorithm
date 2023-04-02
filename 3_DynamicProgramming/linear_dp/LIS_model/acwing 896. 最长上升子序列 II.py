n = int(input())
nums = list(map(int, input().split()))
tail = []

for num in nums:
    if not tail or tail[-1] < num:
        tail.append(num)
    else:
        l, r = 0, len(tail) - 1
        while l < r:
            mid = l + r >> 1
            if tail[mid] >= num: r = mid
            else: l = mid + 1
        tail[r] = num

print(len(tail))