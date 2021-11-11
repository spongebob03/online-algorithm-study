#https://www.acmicpc.net/problem/2156

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))

dp = [0] * (n+1)

# 1, 2에 대한 예외처리를 안해주면 런타임 에러 발생
if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

if n >= 3:
    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])
        
print(dp[-1])