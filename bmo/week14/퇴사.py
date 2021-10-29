f = open('bmo/week14/input3.txt')
n = int(f.readline())
t = []
q = []
dp = [0] * (n+1)
max_value = 0

for i in range(1, n+1):
    x, y = map(int, f.readline().split())
    t.append(x)
    q.append(y)

for i in range(n - 1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)