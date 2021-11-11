#https://www.acmicpc.net/problem/1695
#https://stillchobo.tistory.com/105

def solution(arr, dp, a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    if a >= b:
        dp[a][b] = 0
        return dp[a][b]
    
    if arr[a] == arr[b]:
        dp[a][b] = solution(arr, dp, a+1, b-1)
    else:
        dp[a][b] = min(solution(arr, dp, a, b-1), solution(arr, dp, a+1, b)) + 1

    return dp[a][b]
    
if __name__ == '__main__':
    f = open('bmo/DP/input.txt', 'r')

    n = 5
    arr = [1, 2, 3, 4, 2]

    dp = [[-1] * n for _ in range(n)]
    
    for i in range(n-1):
        for j in range(i+1, n):
            solution(arr, dp, i, j)
    
    print(dp[0][-1])