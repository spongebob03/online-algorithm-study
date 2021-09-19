# 기둥 설치
def build_gi(coord, space):
    x,y = coord
    valid = False 
    # 설치 가능한 조건: 바닥이거나, 또는 한 쪽 끝에 기둥 또는 보 
    if y == 0 or 2 in space[x][y] or 3 in space[x][y] or 4 in space[x][y]:
        space[x][y] += [1]
        space[x][y+1] += [2]
        valid = True
    return space, valid

# 보 설치
def build_bo(coord, space):
    x,y = coord 
    valid = False 
    # 설치 가능한 조건: 적어도 한 쪽 끝에 기둥, 또는 양쪽 끝에 보 
    if (2 in space[x][y] + space[x+1][y]) or ((3 in space[x][y] or 4 in space[x][y]) and 3 in space[x+1][y] or 4 in space[x+1][y]):
        space[x][y] += [3]
        space[x+1][y] += [4]
        valid = True
    return space, valid
    
# 기둥 삭제
def del_gi(coord, space):
    x,y = coord
    valid = False 
    # 삭제 불가능한 조건 (1) 기둥 위에 기둥이 있는 경우
    if 1 in space[x][y+1]:
        return space, valid
    # 삭제 불가능한 조건 (2) 기둥 위에 보가 있고 보의 다른 쪽에 기둥이 없는 경우 
    # 단, 기둥 위에 보가 2개 있어서 서로 잡아주는 상황이면 삭제 가능 
    elif 3 in space[x][y+1] and 1 not in space[x+1][y+1]:
        if not ((3 in space[x][y+1] and 4 in space[x][y+1]) and (3 in space[x-1][y+1] and 4 in space[x-1][y+1]) and (3 in space[x+1][y+1] and 4 in space[x+1][y+1])):
            return space, valid
        
    space[x][y].remove(1)
    space[x][y+1].remove(2)
    valid = True
    
    return space, valid

    
# 보 삭제
def del_bo(coord, space):
    x,y = coord
    valid = False 
    # 삭제 불가능한 조건 (1) 보 위에 기둥이 있는 경우
    # 단, 바닥이 아니고 밑에 다른 기둥도 없음
    if y != 0:
        if 2 not in space[x][y] and 1 in space[x][y]:
            return space, valid
        if 2 not in space[x+1][y] and 1 in space[x+1][y]:
            return space, valid
    # 삭제 불가능한 조건 (2) 보 위에 보가 있는 경우
    # 이때, 위에 있는 보가 다른 기눙에 기대지 않은 경우 
    if space[x][y].count(3) + space[x][y].count(4) >= 2 and 2 not in space[x][y] and 2 not in space[x-1][y]:
        return space, valid
    if space[x+1][y].count(3) + space[x+1][y].count(4) >= 2 and 2 not in space[x+1][y] and 2 not in space[x+2][y]:
        return space, valid

    space[x][y].remove(3)
    space[x+1][y].remove(4)
    valid = True
    return space, valid
    

def solution(n, build_frame):
    space = [[[] for _ in range(n+1)] for _ in range(n+1)] 
    answer = []
    
    for b in build_frame:
        # 좌표
        coord = b[:2]
        # 기둥 삭제 
        if b[2:] == [0,0]:
            space, valid = del_gi(coord, space)
            if valid:
                answer.remove(b[:-1])
        # 기둥 설치
        elif b[2:] == [0,1]:
            space, valid = build_gi(coord, space)
            if valid:
                answer.append(b[:-1])
        # 보 삭제
        elif b[2:] == [1,0]:
            space, valid = del_bo(coord, space)
            if valid:
                answer.remove(b[:-1])
        # 보 설치
        else:
            space, valid = build_bo(coord, space)
            if valid:
                answer.append(b[:-1])
                
    answer.sort()
    return answer