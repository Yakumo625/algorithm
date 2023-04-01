n, m = map(int, input().split())
a, b = (input() for _ in range(2))
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]: dp[i][j] = dp[i - 1][j - 1] + 1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j - 1])
    #     print(*dp, sep='\n')
    #     print()
    # print()

print(*dp, sep='\n')
print(dp[n - 1][m - 1])



# 30 50
# yagdazddszvxoohdxntchoconxuuyw
# oyignzcpgpelpltgoltszeaayugamlcrteuradbkqfvbeqeyrs