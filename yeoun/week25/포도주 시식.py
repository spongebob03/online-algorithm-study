import sys

n = int(sys.stdin.readline())
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

if n < 3:
    print(sum(wine))

else:
	dp = [0] * n

	dp[0] = wine[0]
	dp[1] = dp[0] + wine[1]
	dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

	if n > 3:
		for i in range(3, n):
			# i번째 포도주를 마신 경우
				# i-1, i번째 포도주를 마신 경우: dp[i - 3] + wine[i - 1] + wine[i]
				# i-1번째 포도주는 마시지 않고 i번째 포도주만 마신 경우: dp[i - 2] + wine[i]
			# i번째 포도주를 마시지 않은 경우: dp[i-1]
			dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 1])

	print(dp[-1])