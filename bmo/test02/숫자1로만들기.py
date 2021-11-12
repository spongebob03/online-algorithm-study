n = 10
INF = 1e9
dp = [0] * (n+1)
dp[1] = 0
history = [set([i, 1]) for i in range(n+1)]

for i in range(2, n+1):
    count = INF
    nums = set()
    if i % 3 == 0 and count > dp[i // 3] + 1:
        count = dp[i // 3] + 1
        nums = history[i // 3]
    if i % 2 == 0 and count > dp[i // 2] + 1:
        count = dp[i // 2] + 1
        nums = history[i // 2]
    if count > dp[i - 1] + 1 and count > dp[i - 1] + 1:
        count = dp[i - 1] + 1
        nums = history[i - 1]
    dp[i] = count
    history[i] |= nums

print(dp[-1])
for num in sorted(list(history[-1]), reverse=True):
    print(num, end=' ')