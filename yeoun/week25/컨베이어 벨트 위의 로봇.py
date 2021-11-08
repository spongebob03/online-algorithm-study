# 틀림
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split()))) # 각 칸의 내구도 
robots = [] # 로봇이 있는 칸의 인덱스 

# 컨베이어 벨트의 회전
def rotate(belt, robots):
	last = belt.pop()
	belt.appendleft(last)
	# 로봇도 한 칸씩 이동 (단, 내리는 부분에 도달하면 바로 내리기)
	robots = [(robot+1)%(2*N) for robot in robots if (robot+1)%(2*N) != N-1]
	return belt, robots

# 로봇의 이동
def robot_move(belt, robots):
	for i, robot in enumerate(robots):
		next_idx = (robot+1)%(2*N)
		# 다음 칸에 로봇이 없고 내구도가 0보다 크면 
		if next_idx not in robots and belt[next_idx] > 0:
			robots[i] = next_idx # 다음 칸으로 이동
			belt[next_idx] -= 1 # 다음 칸의 내구도 1 감소 
			if next_idx == N-1: # 다음 칸이 내리는 칸이면 내리기 
				del robots[i]
	return belt, robots

# 로봇 올리기 
def robot_load(belt, robots):
	# 올리는 칸에 로봇이 없고 내구도가 0보다 크면
	if belt[0] > 0 and 0 not in robots:
		belt[0] -= 1 # 올리는 칸의 내구도 1 감소 
		robots.append(0) # 로봇 올리기 
	return belt, robots

# 내구도 0인 칸이 K개 이상이면 True 
def end_condition(belt, K):
	if len([i for i, b in enumerate(belt) if b == 0]) >= K:
		return True
	return False


level = 1
while True:
	belt, robots = rotate(belt, robots)
	belt, robots = robot_move(belt, robots)
	belt, robots = robot_load(belt, robots)
	if end_condition(belt, K):
		break
	level += 1

print(level)

