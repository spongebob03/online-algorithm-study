f = open('bmo/week20/input4.txt','r')
n, k = map(int, f.readline().split())

weights = [0]
values = [0]

for _ in range(n):
    w, v = map(int, f.readline().split())
    weights.append(w)
    values.append(v)

d = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if (j - weights[i] >= 0):
            d[i][j] = max(d[i-1][j], d[i-1][j-weights[i]] + values[i])

print(d[n][k])