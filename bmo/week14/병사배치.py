def solution(powers):
    dp = [1] * len(powers)

    for i in range(1, len(powers)):
        for j in range(i, -1, -1):
            if powers[j] > powers[i]:
                dp[i] = dp[j] + 1
                break

    return len(powers) - max(dp)

if __name__ == '__main__':
    n = int(input())
    powers = list(map(int, input().split()))
    result = solution(powers)
    print(result)