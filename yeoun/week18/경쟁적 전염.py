import sys
from collections import defaultdict, deque

# N: 시험관의 크기
# K: 바이러스의 종류
N, K = map(int, sys.stdin.readline().split())

# 시험관
graph = []
# key: 바이러스 번호, value: 바이러스 좌표들의 리스트  
virus = defaultdict(deque)

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j, v in enumerate(row):
        if v > 0:
            virus[v].append((i,j))
    graph.append(row)

# S초 후 (x,y) 좌표의 상태
S, x, y = map(int, sys.stdin.readline().split())
# 상하좌우
UDLR = [(-1,0), (1,0), (0,-1), (0,1)]

def contaminate(graph, virus, K):
    # 1초 후 바이러스들의 좌표 
    next_virus = defaultdict(deque)
    # 1~K 바이러스 차례대로 
    for v in range(1, K+1):
        if v in virus:
            while virus[v]:
                current = virus[v].popleft()
                # 현재 바이러스의 상하좌우 좌표 
                pos = []
                for udlr in UDLR:
                    pos.append(tuple([sum(x) for x in zip(current, udlr)]))
                for p in pos:
                    a,b = p
                    # N*N 안에 있고 현재 비어있으면 전염 
                    if a in range(0,N) and b in range(0,N) and graph[a][b] == 0:
                        graph[a][b] = v
                        next_virus[v].append((a,b))
    return graph, next_virus

# S초까지 반복 
second = 1
while second <= S:
    graph, virus = contaminate(graph, virus, K)
    second += 1

print(graph[x-1][y-1])
