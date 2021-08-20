from itertools import permutations

n = 5
coins = [3, 2, 1, 1, 9]

candidate = [0 for _ in range(sum(coins)+1)]

candidate[0] = 1
candidate[-1] = 1

for i in range(1, n):
    for combi in permutations(coins, i):
        candidate[sum(combi)] += 1

print(f'주어진 동전들로 만들 수 없는 양의 정수: {candidate.index(0)}')