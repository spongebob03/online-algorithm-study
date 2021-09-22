import sys
from itertools import combinations
from collections import deque
import copy

N = int(sys.stdin.readline())
school = [] # 초기 학교 상태 (선생님, 학생, 빈 곳만 있는 상태)
teachers = []  # 선생님들의 위치
blank = []  # 빈 곳의 좌표
for i in range(N):
    row = sys.stdin.readline().split()
    for j, r in enumerate(row):
        if r == 'T':
            teachers.append((i, j))
        elif r == 'X':
            blank.append((i, j))
    school.append(row)

# 상하좌우
UDLR = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 선생님들이 감시할 수 있는 범위 계산
def teacher_detect(school, teacher, N):
    # 각 상하좌우 방향에 대해 
    for udlr in UDLR:
        q = deque([teacher])
        while q:
            cur = q.popleft()
            a, b = cur
            x, y = udlr # 현재 방향으로 쭉 이동 
            # index error가 나지 않는지 
            if (a + x) in range(N) and (b + y) in range(N):
                pos = school[a + x][b + y]
                if pos == 'S': # 학생이 있으면 걸림 
                    return True
                elif pos == 'O': # 장애물 있으면 이 방향으로 볼 수 있는 범위는 끝 
                    break
                elif pos == 'X': # 빈 곳이면 계속 이 방향으로 이동 
                    q.append((a + x, b + y))
    return False


# 주어진 장애물 위치에 따라 학생들이 감시를 피할 수 있는지 여부 확인
def teachers_detect(new_school, teachers, N):
    # 각 선생님에 대해 
    for teacher in teachers:
        # 걸린 학생이 한 명이라도 있는 경우 
        if teacher_detect(new_school, teacher, N):
            return 'detected'
    # 모든 학생이 걸리지 않은 경우 
    return 'undetected'


# 모든 빈 곳 중 3개 선택
combs = list(combinations(blank, 3))

success_flag = False
for comb in combs:
    new_school = copy.deepcopy(school)  # deepcopy
    # 현재 combination으로 장애물 세우기
    for c in comb:
        a, b = c
        new_school[a][b] = 'O'
    # 현재 combination으로 모든 학생이 걸리지 않은 경우 success
    if teachers_detect(new_school, teachers, N) == 'undetected':
        success_flag = True
        break

# success면 YES, 아니면 NO 출력 
if success_flag:
    print('YES')
else:
    print('NO')

