from collections import deque

f = open('bmo/week21/input.txt', 'r')

def get_pos(graph, num):
    for i in range(4):
        if num in graph[i]:
            return (i, graph[i].index(num))

def valid (x, y):
    return 0 <= x < 4 and 0 <= y < 4

    
# 물고기 번호: 물고기별 방향 (1~8)
# 0번 물고기는 상어, 빈칸
# 0번 방향은 물고기가 없는 것
fish = {i: 0 for i in range(16+1)}
DELTAS = {1: (-1, 0), 2:(-1, -1), 3:(0, -1), 4: (0, -1), 5:(1, 0), 6:(1, 1), 7:(0, 1), 8:(-1, 1)}
graph = []

for _ in range(4):
    row = []
    data = list(map(int, f.readline().split()))
    for num, direction in zip(data[::2], data[1::2]):
        row.append(num)
        fish[num] = direction
    graph.append(row)


# 처음 상어 이동
shark = (0, 0)
fish[0] = fish[graph[0][0]] # 상어의 방향

graph[0][0] = 0

# 물고기들 이동
for i in range(1, 16+1):
    if fish[i] == 0:
        continue
    x, y = get_pos(graph, i)

    dx, dy = DELTAS[fish[i]]
    next_x = x + dx
    next_y = y + dy

    while not valid(next_x, next_y) or (next_x, next_y) in shark:
        fish[i] = (fish[i] + 1) % 8

        dx, dy = DELTAS[fish[i]]
        print(dx, dy)
        next_x = x + dx
        next_y = y + dy
    
    graph[x][y], graph[next_x][next_y] = graph[next_x][next_y], graph[x][y]
