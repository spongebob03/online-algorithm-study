f = open('bmo/week22/input1.txt', 'r')
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4

def print_graph(graph):
    for row in graph:
        print(row)
def valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def trans(x, y, direction, n):
    DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    dx, dy = DELTAS[direction]
    nx = x + dx
    ny = y + dy
    
    if not valid(nx, ny, n):
        return None
    # 이동할 위치에 이미 냄새가 있는지 
    # 다른 상어 현재 있지 
    return (x + dx, y + dy)


if __name__ == '__main__':
    n, m, k = map(int, f.readline().split())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, f.readline().split())))
    #각 상어의 현재 방향
    direction = {i:d for i, d in enumerate(list(map(int, f.readline().split())), 1)}
    #각 상어의 현재 위치
    position = {}
    for r in range(n):
        for c in range(n):
            status = graph[r][c]
            if status != 0:
                position[status] = (r, c)
    # 냄새...graph[r][c] = i로? 

    #각 상어의 방향별 우선순위 방향
    priority = {}
    for i in range(1, m+1):
        priority[i] = []
        for j in range(4):
            priority[i].append(list(map(int, f.readline().split())))

    print_graph(graph)
    # print(direction)
    # print(position)
    # print(priority)

    # 상어 이동방향 결정
    for i in range(1, m+1):
        curr_pos = position[i]
        curr_dir = direction[i]


