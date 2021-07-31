def solution(n, powers):
    dp = [[power] for power in powers]
    max_power = 0
    answer = 0

    for i in range(1, n):
        for j in range(i, -1, -1):
            if powers[j] > powers[i]:
                dp[i] = dp[j] + dp[i]
                break
    
    for i in range(n):
        if max_power < sum(dp[i]):
            answer = n - len(dp[i])
            
    return answer

if __name__ == '__main__':
    n = 7
    powers = [15, 11, 4, 8, 5, 2, 4]
    result = solution(n, powers)
    print(result)