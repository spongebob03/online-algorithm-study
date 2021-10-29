def solution(n, powers):
    dp = [1] * n
    powers.reverse()

    for i in range(1, n):
        for j in range(0, i):
            if powers[j] < powers[i]:
                dp[i] = max(dp[i], dp[j]+1)

    return n - max(dp)

if __name__ == '__main__':
    n = 7
    powers = [15, 11, 4, 8, 5, 2, 4]
    result = solution(n, powers)
    print(result)