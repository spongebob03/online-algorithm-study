# python 시간 초과, pypy3 통과
import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))
visited = [[False] * N for _ in range(N)]


# 상하좌우
UDLR = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 국경선 열리는 나라들 구하기 
def find_union(world, N, L, R, unions):
    # 모든 좌표에 대해 
    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않은 경우 
            if not visited[i][j]:
                q = deque([(i,j)])
                while q:
                    cur = q.popleft()
                    # 현재 좌표의 상하좌우
                    pos = []
                    for udlr in UDLR:
                        a,b = cur
                        x,y = udlr
                        pos.append((a+x, b+y))
                    for p in pos:
                        # 0~N 안에 있고 아직 방문하지 않은 경우 
                        if p[0] in range(N) and p[1] in range(N) and not visited[p[0]][p[1]]:
                            # cur와 상하좌우의 인구 수 차이 
                            diff = abs(world[cur[0]][cur[1]] - world[p[0]][p[1]])
                            if L <= diff and diff <= R:
                                # 방문 후 큐에 추가 
                                visited[p[0]][p[1]] = True
                                q.append(p)
                                already = False
                                # cur가 이미 다른 나라와 union인 경우, 그 union에 p 추가 
                                for num, union in enumerate(unions):
                                    if (i,j) in union:
                                        unions[num] += [p]
                                        already = True
                                # cur의 첫 union인 경우 cur, p를 unions 안의 새로운 list로 추가 
                                if not already:
                                    unions.append([cur, p])
    return unions

days = 0
# unions: list of list
# ex. (0,0)과 (1,0)이 국경을 열고 (2,1), (2,2)가 국경을 연다면, unions = [[(0,0),(1,0)], [(2,1),(2,2)]]
unions = find_union(world, N, L, R, unions=[])

# 국경을 열 수 있는 상태면 계속 반복 
while unions:
    # 인구 이동 날짜 더하기 
    days += 1
    # 각 연합국들에 대해 
    for union in unions:
        # 중복 제거 
        union = list(set(union))
        # 연합국의 총 인구 수 
        sum = 0
        for pos in union:
            sum += world[pos[0]][pos[1]]
        # 연합국의 새로운 인구 수 
        new_val = int(sum / len(union))
        # 연합국 인구 수 갱신
        for pos in union:
            world[pos[0]][pos[1]] = new_val

    # visited 초기화 
    visited = [[False] * N for _ in range(N)]
    unions = find_union(world, N, L, R, unions=[])

print(days)
