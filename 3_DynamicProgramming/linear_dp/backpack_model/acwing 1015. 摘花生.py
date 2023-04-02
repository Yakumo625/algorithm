for _ in range(int(input())):
    r, c = map(int, input().split())
    w = [[0] + list(map(int, input().split())) for _ in range(r)]
    w[:0] = [[0] * (c + 1)]
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + w[i][j]
    
    print(dp[r][c])