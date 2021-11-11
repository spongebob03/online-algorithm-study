#https://www.acmicpc.net/problem/20055
from collections import deque

def move_belt(up, down, robot):
    # 컨베이어벨트 한 칸 이동
    down.append(up.pop())
    robot.insert(0, False) # 로봇도 이동. 칸 그대로 움직이기 때문에 로봇이동과 다름
    robot.pop() 
    up.insert(0, down.popleft())

def move_robot(x, robot, up):
    # 앞에 로봇있는지(robot배열) and 내구도 (up, 어차피 위쪽에만 올릴 수 있다)
    n = len(robot)
    for i in range(x+1, n):
        if not robot[i] and up[i] > 0:
            # 로봇 이동
            robot[x], robot[i] = False, True
            up[i] -= 1
        else:
            break

if __name__ == '__main__':
    f = open('bmo/input.txt', 'r')

    n, k = map(int, f.readline().split())
    A = list(map(int, f.readline().split()))
    up = A[:n]
    down = deque(A[n:])
    robot = [False] * n
    answer = 0

    while True:
        answer += 1
        # 0. 올리는 위치에 로봇 올리기
        if up[0] > 0:
            up[0] -= 1
            robot[0] = True
        # 1. 컨베이어벨트 이동
        move_belt(up, down, robot)
        # 내릴 수 있는 위치에 로봇 있는지 확인
        robot[-1] = False

        # 2. 로봇 이동 (로봇 위치 저장 어떻게 할것인가) n길이의 배열로 표시
        for r in range(n-1, 0, -1):
            if robot[r]:
                move_robot(r, robot, up)
            # 내릴 수 있는 위치에 로봇이 있는지 확인
            robot[-1] = False
       
        if up.count(0) + down.count(0) >= k:
            print(answer)
            break
