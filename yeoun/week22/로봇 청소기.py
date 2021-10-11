import sys

N, M = map(int, sys.stdin.readline().split())
x,y, direction = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
	graph.append(list(map(int, sys.stdin.readline().split())))
visited = [[False]*M for _ in range(N)]

# 방향 전환
left_dict = {0:3, 1:0, 2:1, 3:2} # 왼쪽 회전 
rear_dict = {0:2, 1:3, 2:0, 3:1} # 후진 
move_dict = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

answer = 1
left_rotation = 0

while True:
	visited[x][y] = True
	dx, dy = move_dict[left_dict[direction]]
	# 2a: 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
	if graph[x+dx][y+dy] == 0 and not visited[x+dx][y+dy]:
		x += dx
		y += dy
		direction = left_dict[direction]
		left_rotation = 0
		answer += 1
	else:
		# 2b: 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
		if left_rotation < 4:
			direction = left_dict[direction]
			left_rotation += 1
			continue
		else:
			dx, dy = move_dict[rear_dict[direction]]
			# 2c: 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
			if graph[x+dx][y+dy] == 0:
				x += dx
				y += dy
				left_rotation = 0
				continue
			# 2d: 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
			else:
				break

print(answer)