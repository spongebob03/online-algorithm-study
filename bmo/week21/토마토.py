from collections import deque

def valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n
    
if __name__ == '__main__':
    answer = 0
    f = open('bmo/week21/input2.txt', 'r')
    n, m = map(int, f.readline().split())

    queue = deque()
    board = []
    for _ in range(m):
        board.append(list(map(int, f.readline().split())))

    visited = [[False] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == -1:
                visited[i][j] = True
            elif board[i][j] == 1:
                visited[i][j] = True
                queue.append((i, j, 0))
    
    while queue:
        x, y, day = queue.popleft()

        DELTAS = ((0, 1), (0, -1), (-1, 0), (1, 0))
        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy
            next_day = day + 1

            if valid(next_x, next_y, m, n) and not visited[next_x][next_y] and board[next_x][next_y] == 0:
                visited[next_x][next_y] = True
                queue.append((next_x, next_y, next_day))
                answer = next_day

    success = True
    for row in visited:
        if not all(row):
            success = False
    
    print(answer) if success else print(-1)
