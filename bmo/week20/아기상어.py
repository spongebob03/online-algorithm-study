from collections import deque

f = open('bmo/week20/input2.txt','r')

def bfs(space, x, y, baby_shark):
    n = len(space)
    d = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    d[x][y] = 0

    while queue:
        x, y = queue.popleft()
        DELTAS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for dx, dy in DELTAS:
            nx = x + dx
            ny = y + dy
            
if __name__ == '__main__':
    answer = 0
    space = []
    n = int(f.readline())
    for _ in range(n):
        space.append(list(map(int, f.readline().split())))

    shark = 2 # 처음 아기 상어의 크기 
    x, y = 0, 0

    # 아기 상어 처음 위치 찾기

    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                x, y = i, y
                space[i][j] = 0 

    