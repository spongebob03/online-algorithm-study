import sys

# 병사 수
N = int(sys.stdin.readline())
# 병사들의 전투력
soldiers = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

# 0 <= j < i 
# dp[i] = max(dp[i], dp[j]+1) if soldiers[j] > soldiers[i]
for i in range(N):
    for j in range(i):
        # 내림차순이면 
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

# max(dp)는 가장 긴 내림차순 부분 수열의 길이 
print(N - max(dp))