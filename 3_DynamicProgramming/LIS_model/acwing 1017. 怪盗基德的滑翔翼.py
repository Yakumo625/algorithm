for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    dp1, dp2 = [1] * n, [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]: dp1[i] = max(dp1[i], dp1[j] + 1)
            if nums[j] > nums[i]: dp2[i] = max(dp2[i], dp2[j] + 1)
    
    print(max(max(dp1), max(dp2)))