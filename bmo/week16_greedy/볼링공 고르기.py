from itertools import combinations

n, m = 8, 5
balls = [1, 5, 4, 3, 2, 4, 5, 2]

cnt = 0
for combi in combinations([i for i in range(n)], 2):
    if balls[combi[0]] == balls[combi[1]]:
        continue
    cnt += 1

print(cnt)