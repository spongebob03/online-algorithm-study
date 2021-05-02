def solution(dirs):
    answer = 0
    pos = (0,0) # 시작점 
    hist = []

    movement = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    
    for d in dirs:
        x, y = pos
        dx, dy = movement[d]

        new_pos = (x+dx, y+dy)
        
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