from collections import deque
import math

def valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# 1. 미세 먼저 확산
def bfs(r, c, R, C, graph, visited):
    queue = deque([r, c])
    visited[r][c] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            nx = x + dx
            ny = x + dy
            if valid(nx, ny, R, C) and graph[nx][ny] != -1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = math.round(graph[x][y] / 5)
                graph[x][y] -= math.round(graph[x][y] / 5)
                
def circulate1(r, c, R, C, graph):
    # 위쪽 공기청정기의 바람은 반시계방향
    
    # 들어오는 순으로 처리
    return 0
