f = open('bmo/week14/input3.txt')
n = int(f.readline())
tasks = []
for i in range(1, n+1):
    dur, price = map(int, f.readline().split())
    if i + dur > n + 1:
        continue
    tasks.append((i, i+dur, price))
tasks.sort(key=lambda x: (x[1], -x[2]))
print(tasks)

result = 0
time = 0

for task in tasks:
    start, end, price = task
    if time > start:
        continue
    result += price
    time = end

print(result)