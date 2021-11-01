# PyPy3로 통과 
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 미세먼지 위치 양 
def locate_dust(room, R, C):
	dust = []
	for i in range(R):
		for j in range(C):
			if room[i][j] > 0:
				dust.append((i,j,room[i][j]))
	return dust

# 미세먼지의 확산
def spread_dust(room,R,C,loc):
	x,y, score = loc
	count = 0
	for a,b in zip(dx,dy):
		if x+a in range(R) and y+b in range(C) and room[x+a][y+b] != -1:
			room[x+a][y+b] += score // 5
			count += 1
	room[x][y] -= score//5 * count
	return room

# 공기청정기 윗부분 확산 
def purifier_upper(room,R,C,loc):
	x,y = loc
	for i in range(x-1,0,-1): # ↓
		room[i][0] = room[i-1][0]
	for i in range(0,C-1): # ←
		room[0][i] = room[0][i+1]
	for i in range(0,x): # ↑
		room[i][C-1] = room[i+1][C-1]
	for i in range(C-1,1,-1): # →
		room[x][i] = room[x][i-1]
	room[x][1] = 0 # 미세먼지 없는 바람
	return room

# 공기청정기 아랫부분 확산 
def purifier_lower(room,R,C,loc):
	x,y = loc
	for i in range(x+1,R-1): # ↑
		room[i][0] = room[i+1][0]
	for i in range(0,C-1): # ←
		room[R-1][i] = room[R-1][i+1]
	for i in range(R-1, x, -1): # ↓
		room[i][C-1] = room[i-1][C-1]
	for i in range(C-1,1,-1): # →
		room[x][i] = room[x][i-1]
	room[x][1] = 0 # 미세먼지 없는 바람
	return room

R,C,T = map(int, sys.stdin.readline().split())

room = []
purifier = [] # 공기청정기의 위치 
for r in range(R):
	row = list(map(int, sys.stdin.readline().split()))
	room.append(row)
	if -1 in row:
		purifier.append((r, row.index(-1)))

# T초간 반복
now = 0
while now < T:
	locs = locate_dust(room, R, C)
	for loc in locs:
		room = spread_dust(room,R,C,loc)
	room = purifier_upper(room,R,C,purifier[0])
	room = purifier_lower(room,R,C,purifier[1])
	now += 1

# 공기청정기 -2는 더해주기
print(sum([sum(r) for r in room])+2)