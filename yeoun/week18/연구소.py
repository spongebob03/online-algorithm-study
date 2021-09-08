import sys
from itertools import combinations
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().split())
graph = [] # 연구소
blank = [] # 벽을 세울 수 있는 빈 곳의 좌표
virus = [] # 바이러스의 좌표
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j, x in enumerate(row):
        if x == 0:
            blank.append((i,j))
        if x == 2:
            virus.append((i,j))
    graph.append(row)

# 상하좌우
UDLR = [(-1,0), (1,0), (0,1), (0,-1)]
# 주어진 연구소 상태에 따라 안전한 곳의 너비를 계산
def compute_safe(graph, virus, N, M):
    q = deque(virus)
    while q:
        cur = q.popleft()
        pos = []
        for udlr in UDLR:
            pos.append(tuple([sum(x) for x in zip(cur, udlr)]))
        for p in pos:
            a,b = p
            if a in range(0,N) and b in range(0,M) and graph[a][b] == 0:
                graph[a][b] = 2
                q.append((a,b))
    ans = 0
    for row in graph:
        ans += row.count(0)
    return ans

# 모든 빈 곳 중 3개 선택
combs = list(combinations(blank, 3))

# 안전한 너비의 최댓값
max_safe = 0
for comb in combs:
    # new_graph = [x[:] for x in graph]
    new_graph = copy.deepcopy(graph) # deepcopy
    # 현재 combination으로 벽 세우기
    for c in comb:
        a,b = c
        new_graph[a][b] = 1
    max_safe = max(max_safe, compute_safe(new_graph, virus, N, M))

print(max_safe)
