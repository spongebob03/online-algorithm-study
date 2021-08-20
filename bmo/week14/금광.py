f = open('bmo/week14/input1.txt')
tc = int(f.readline())
for _ in range(tc):
    n, m = map(int, f.readline().split())
    dp = [[0] * m for _ in range(n)]
    table = list(map(int, f.readline().split()))
    for i in range(n):
        dp[i] = table[i*m:i*m+m]

    result = 0
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] += max(dp[i][j-1], dp[i+1][j-1])
            elif i == n-1:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1])
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
            if j == m-1:
                result = max(result, dp[i][j])
                
    print(result)