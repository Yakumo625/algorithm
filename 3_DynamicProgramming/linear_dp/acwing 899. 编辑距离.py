n, m = map(int, input().split())
s1s = [' ' + input() for _ in range(n)]

for _ in range(m):
    s2, t = input().split()
    s2 = ' ' + s2
    res = 0
    for s1 in s1s:
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2) for _ in range(l1)]
        
        for i in range(1, l2): dp[0][i] = i
        for i in range(1, l1): dp[i][0] = i
        
        for i in range(1, l1):
            for j in range(1, l2):
                if s1[i] == s2[j]: dp[i][j] = dp[i - 1][j - 1]
                else: dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        
        if dp[l1 - 1][l2 - 1] <= int(t): res += 1
    print(res)