import sys

# 퇴사 전 남은 일 수
N = int(sys.stdin.readline())
dp = [0] * (N+1)

for i in range(N):
    # 소요일자, 이익 
    t, profit = list(map(int, sys.stdin.readline().split()))
    # 일이 끝나는 날, 일이 시작되는 날
    end, start = i+t, i+1

    if end in range(len(dp)) and start-1 in range(len(dp)):
        # (현재 일이 시작되기 전까지의 이익 + 현재 일을 끝낸 후의 이익)과 (일이 끝나는 날의 기존 dp 값) 중 큰 값을 취함  
        dp[end] = max(dp[start-1] + profit, dp[end])
        # 이익이 줄어들 수는 없으므로 
        for j in range(end+1, len(dp)):
            dp[j] = max(dp[j], dp[end])

# 마지막 날의 최대 이익 
print(dp[-1])