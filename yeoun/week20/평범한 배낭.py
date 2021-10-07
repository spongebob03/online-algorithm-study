# 참고: https://chanhuiseok.github.io/posts/improve-6/
import sys

N, K = map(int, sys.stdin.readline().split())

things = []
for _ in range(N):
	W, V = map(int, sys.stdin.readline().split())
	things.append((W,V))


# 0 - K
dp = [0] * (K+1)
for thing in things:
	W, V = thing
	for i in range(len(dp)-1,-1,-1):
		if i-W >= 0:
			dp[i] = max(dp[i], dp[i-W] + V)
		else:
			break

print(max(dp))

