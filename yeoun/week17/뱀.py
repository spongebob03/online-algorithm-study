import sys

# 보드 크기
N = int(sys.stdin.readline())
# 1 ~ N
board = [[0] * (N+1) for _ in range(N+1)]

# 사과 개수
K = int(sys.stdin.readline())
apples = []
for i in range(K):
    apples.append(list(map(int, sys.stdin.readline().split())))

# 방향 변환 횟수
L = int(sys.stdin.readline())
turn = {}
for i in range(L):
    second, direction = sys.stdin.readline().split()
    # n초 '후'에 방향 전환이므로 +1
    turn[int(second)+1] = direction

head = [1,1] # 뱀의 머리 위치
snake = [[1,1]] # 뱀의 전체 몸통 위치
now = 0 # 현재 시각
direction = [0,1] # 현재 방향 (오른쪽으로 초기화)

# 오른쪽 방향 전환
right_turn = {(-1,0):(0,1), (1,0):(0,-1), (0,-1):(-1,0), (0,1):(1,0)}
# 왼쪽 방향 전환
left_turn = {(-1,0):(0,-1), (1,0):(0,1), (0,-1):(1,0), (0,1):(-1,0)}



while True:
    now += 1
    if now in turn.keys():
        if turn[now] == 'D': # 오른쪽
            direction = right_turn[tuple(direction)]
        else: # 왼쪽
            direction = left_turn[tuple(direction)]
    # 뱀 머리 방향대로 이동
    pre_head = head
    head = [x+y for x,y in zip(head, direction)]

    # 뱀의 머리가 몸통에 닿는 경우
    if head in snake:
        break

    # 뱀 나머지 부분 방향대로 이동
    # 사과가 있는 곳으로 이동한 경우
    if head in apples:
        apples.remove(head)
        snake = [head] + snake
    # 사과가 없는 경우
    else:
        snake = [head] + snake
        snake.pop(-1)

    # 보드 끝에 다다름
    if head[0] < 1 or head[0] > N or head[1] < 1 or head[1] > N:
        break

print(now)



