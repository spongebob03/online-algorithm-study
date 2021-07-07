import fileinput
import heapq

INF = int(1e9)

# 입력 처리하기
nextN = 1
spaces = []
for i, line in enumerate(fileinput.input()):
    if i == 0:
        continue
    elif i == nextN:
        N = int(line)
        spaces.append([])
        nextN += N + 1
    else:
        spaces[-1].append(list(map(int, line.split())))

# 다익스트라 알고리즘
def explore(space):
    N = len(space)
    # N * N
    distance = [[INF]*N for _ in range(N)]
    q = []
    # (0,0)에서 시작
    heapq.heappush(q, (0, (0,0)))
    distance[0][0] = 0
    while q:
        dist, now = heapq.heappop(q)
        x,y = now
        if distance[x][y] < dist:
            continue
        # 상, 하, 좌, 우
        adjs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for adj in adjs:
            a, b = adj
            if a in range(0,N) and b in range(0,N):
                cost = dist + space[a][b]
                if cost < distance[a][b]:
                    distance[a][b] = cost
                    heapq.heappush(q, (cost, (a,b)))

    # (N-1, N-1)까지 가는데 소모되는 에너지 + (0,0)을 지나는데 소모되는 에너지
    return distance[N-1][N-1] + space[0][0]

for space in spaces:
    print(explore(space))