import sys
from itertools import combinations

# N: 도시 크기
# M: 최종 선택할 치킨가게 개수 
N, M = map(int, sys.stdin.readline().split())
city = []
houses = []  # 집 좌표
stores = []  # 치킨가게 좌표
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if row[j] == 1:
            houses.append((i + 1, j + 1))
        if row[j] == 2:
            stores.append((i + 1, j + 1))
    city.append(row)

# 각 집마다 각 치킨가게까지의 거리를 저장한 딕셔너리 
dist = {}
for house in houses:
    x, y = house
    dist[house] = []
    for store in stores:
        a, b = store
        dist[house].append(abs(x - a) + abs(y - b))

# 존재하는 모든 치킨가게를 선택할 경우 
if len(stores) == M:
    answer = 0
    for h in dist:
        # 각 집마다의 거리 중 최소 거리를 더해 답으로 반환
        answer += min(dist[h])
    print(answer)
# 일부 치킨가게만 선택할 경우 
else:
    # M개를 선택하는 모든 경우의 수에 따른 치킨 거리
    combs = list(combinations(list(range(len(stores))), M))
    candidates = []
    for comb in combs:
        ans = 0
        for h in dist:
            ans += min([dist[h][idx] for idx in comb])
        candidates.append(ans)
    # 모든 치킨 거리 중 최솟값을 답으로 반환
    print(min(candidates))



