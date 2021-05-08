def solution(m, n, puddles):
    puddles = set((y, x) for x, y in puddles)
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if (i, j) in puddles or (i, j) == (1, 1):
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007

    return dp[-1][-1]