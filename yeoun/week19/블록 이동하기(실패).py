from collections import deque

def next_move(board, robot):
    N = len(board)
    r1, r2 = robot 
    result = []
    # 가로로 놓여 있는 경우 
    if r1[0] == r2[0] and r1[1] + 1 == r2[1]:
        # 아래로 평행 이동, 아래 오른쪽 방향으로 회전, 아래 왼쪽 방향으로 회전 
        if r1[0]+1 in range(N) and board[r1[0]+1][r1[1]] == 0 and board[r2[0]+1][r2[1]] == 0:
            result += [[(r1[0]+1,r1[1]),(r2[0]+1,r2[1])], [r2,(r2[0]+1,r2[1])], [r1,(r1[0]+1,r1[1])]]
        # 오른쪽으로 평행 이동 
        if r2[1]+1 in range(N) and board[r2[0]][r2[1]+1] == 0:
            result += [[r2, (r2[0],r2[1]+1)]]
        # 위로 평행 이동, 위 오른쪽 방향으로 회전, 위 왼쪽 방향으로 회전 
        if r1[0]-1 in range(N) and board[r1[0]-1][r1[1]] == 0 and board[r2[0]-1][r2[1]] == 0:
            result += [[(r1[0]-1,r1[1]),(r2[0]-1,r2[1])], [(r2[0]-1,r2[1]),r2], [(r1[0]-1,r1[1]),r1]]
        # 왼쪽으로 평행 이동 
        if r1[1]-1 in range(N) and board[r1[0]][r1[1]-1] == 0:
            result += [[(r1[0],r1[1]-1),r1]]
        
    # 세로로 놓여 있는 경우 
    else:
        # 오른쪽으로 평행 이동, 아래 오른쪽 방향으로 회전, 위 오른쪽 방향으로 회전
        if r1[1]+1 in range(N) and board[r1[0]][r1[1]+1] == 0 and board[r2[0]][r2[1]+1] == 0:
            result += [[(r1[0],r1[1]+1),(r2[0],r2[1]+1)], [r2,(r2[0],r2[1]+1)], [r1,(r1[0],r1[1]+1)]]
        # 왼쪽으로 평행 이동, 아래 왼쪽 방향으로 회전, 위 왼쪽 방향으로 회전
        if r1[1]-1 in range(N) and board[r1[0]][r1[1]-1] == 0 and board[r2[0]][r2[1]-1] == 0:
            result += [[(r1[0],r1[1]-1),(r2[0],r2[1]-1)], [(r2[0],r2[1]-1),r2], [(r1[0],r1[1]-1),r1]]
        # 아래로 평행 이동 
        if r2[0]+1 in range(N) and board[r2[0]+1][r2[1]] == 0:
            result += [[r2,(r2[0]+1,r2[1])]]
        # 위로 평행 이동 
        if r1[0]-1 in range(N) and board[r1[0]-1][r1[1]] == 0:
            result += [[(r1[0]-1, r1[1]),r1]]
    return result
        
def solution(board):
    answer = 0
    N = len(board)
    INF = 10001
    hist = []
    dist = [[INF]*N for _ in range(N)]
    dist[0][0] = 0
    dist[0][1] = 0
    q = deque([[(0,0),(0,1)]])
    while q:
        cur = q.popleft()
        if cur not in hist:
            hist.append(cur)
            for nm in next_move(board, cur):
                q.append(nm)
                dist[nm[-1][0]][nm[-1][1]] = min(dist[nm[-1][0]][nm[-1][1]], dist[cur[-1][0]][cur[-1][1]]+1)
    
    return dist[-1][-1]