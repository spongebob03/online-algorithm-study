f = open('bmo/week17/input1.txt')
n, m = map(int, f.readline().split())

house = []
chicken = []

for i in range(n):
    row = f.readline().split()
    for j in range(n):
        if row[j] == '1':
            house.append((i, j))
        elif row[j] == '2':
            chicken.append((i, j))

street = []
for x1, y1 in house:
    dist = 2 * n
    for x2, y2 in chicken:
        dist = min(dist, abs(x1 - x2) + abs(y1 - y2))
    street.append(dist)

for (x, y), dist in zip(house, street):
    print(f'house ({x},{y}) 치킨거리: {dist}')

street.sort()
print(sum(street[:m])) # ???