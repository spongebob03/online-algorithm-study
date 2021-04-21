def move(pos, direction):
    if direction == 'U': # 위
        return (pos[0], pos[1]+1)
    elif direction == 'D': # 아래 
        return (pos[0], pos[1]-1)
    elif direction == 'R': # 오른쪽 
        return (pos[0]+1, pos[1])
    else: # 왼쪽
        return (pos[0]-1, pos[1])
    
def solution(dirs):
    answer = 0
    pos = (0,0) # 시작점 
    hist = []
    
    for d in dirs:
        new_pos = move(pos, d)
        
        # 좌표평면의 경계를 넘어가는 명령어는 무시
        if new_pos[0] < -5 or new_pos[0] > 5 or new_pos[1] < -5 or new_pos[1] > 5:
            continue
            
        route = [pos, new_pos]
        # 위치 업데이트 
        pos = new_pos
        
        # 반대 방향 포함하여 처음 걸어본 길이면
        if route not in hist and route[::-1] not in hist:
            hist.append(route)
            answer += 1 
   
    return answer