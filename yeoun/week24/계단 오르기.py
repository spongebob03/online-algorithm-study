import sys
N = int(sys.stdin.readline())
scores = []
for _ in range(N):
	scores.append(int(sys.stdin.readline()))

if N < 3:
	print(sum(scores))
else:
	dp = [0] * N
	dp[0] = scores[0]
	dp[1] = scores[0] + scores[1]
	dp[2] = max(scores[0]+scores[2], scores[1]+scores[2])

	for i in range(3,N):
	    dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i-1]+scores[i])

	print(dp[-1])
