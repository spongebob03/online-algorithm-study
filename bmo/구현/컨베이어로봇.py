#https://www.acmicpc.net/problem/20055
from collections import deque

def put_robot(up, robot):
    if up[0] > 0:
        up[0] -= 1
        robot[0] = True

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
        if up[i] > 0 and not robot[i]:
            # 로봇 이동
            robot[x], robot[i] = False, True
            up[i] -= 1
        else:
            break
def print_belt(a, up, down, robot):
    if a == 0:
        print(f'----시작----')
    elif a == 1:
        print(f'----컨베이어 이동----')
    elif a == 2:
        print(f'----로봇 이동----')
    elif a == 3:
        print(f'----로봇 올리기----')
    print(up, end=' ')
    print('로봇 위치', robot)
    print(list(down))
    

if __name__ == '__main__':
    f = open('bmo/input.txt', 'r')

    n, k = map(int, f.readline().split())
    A = list(map(int, f.readline().split()))
    up = A[:n]
    down = deque(A[n:])
    robot = [False] * n
    answer = 0

    # 0. 로봇 올리기
    put_robot(up, robot)
    print_belt(0, up, down, robot)
    while True:
        answer += 1
        print(answer)
        # 1. 컨베이어벨트 이동
        move_belt(up, down, robot)
        print_belt(1, up, down, robot)
        # 내릴 수 있는 위치에 로봇 있는지 확인
        robot[-1] = False

        # 2. 로봇 이동 (로봇 위치 저장 어떻게 할것인가) n길이의 배열로 표시
        for r in range(n-1, -1, -1):
            if robot[r]:
                move_robot(r, robot, up)
                print_belt(2, up, down, robot)
            # 내릴 수 있는 위치에 로봇이 있는지 확인
            robot[-1] = False

        # 3. 올리는 위치에 로봇 올리기
        put_robot(up, robot)
        print_belt(3, up, down, robot)
        if up.count(0) + down.count(0) >= k:
            print(answer)
            break
