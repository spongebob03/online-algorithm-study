import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

storage = [] # 전체 창고 
tomatos = [] # 익은 토마토의 좌표
unripes = 0 # 익지 않은 토마토의 개수 
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    storage.append(row)
    for j in range(M):
        if row[j] == 1:
            tomatos.append((i,j))
        elif row[j] == 0:
            unripes += 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 하루동안 토마토 창고 안에서의 변화
def make_ripe(storage, M, N, tomatos, ripen):
    tomatos = deque(tomatos)
    # 새로 익은 토마토의 좌표 
    new_tomatos = []
    # 각 토마토의 인접한 부분에 0이 있다면 1로 수정하기 
    while tomatos:
        a,b = tomatos.popleft()
        for x,y in zip(dx,dy):
            adj_x, adj_y = a+x, b+y
            if adj_x in range(N) and adj_y in range(M):
                if storage[adj_x][adj_y] == 0:
                    storage[adj_x][adj_y] = 1 # 익게 만들기
                    ripen += 1 
                    new_tomatos.append((adj_x, adj_y))
    return storage, new_tomatos, ripen

days = -1
# 익지 않았다가 익게 된 토마토의 개수 
ripen = 0
while tomatos:
    storage, tomatos, ripen = make_ripe(storage, M, N, tomatos, ripen)
    days += 1

# 처음에 익지 않은 토마토의 개수와 익게 된 토마토의 개수가 같다면 모두 익은 것이므로 days를 출력하지만, 그렇지 않은 경우 아무리 오랜 시간이 지나도 토마토가 익지 못하므로 -1을 출력함
print(days) if unripes == ripen else print(-1)

