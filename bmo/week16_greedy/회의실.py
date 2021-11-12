f = open('bmo/week16_greedy/input1.txt')
n = int(f.readline())
res = []

for _ in range(n):
    s, e = map(int, f.readline().split())
    res.append((s, e))

res.sort(key=lambda x: (x[1], x[0]))
time = 0
count = 0

for reservation in res:
    s, e = reservation
    if time <= s:
        count += 1
        time = e

print(count)