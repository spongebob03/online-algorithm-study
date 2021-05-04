# n = 12일 때 시간 초과

def attackRange(position, n):
    result = []
    x,y = position
    
    # 퀸이 속한 행 
    # result += [(x,i) for i in range(n)] 
    
    # 퀸이 속한 열 
    result += [(i,y) for i in range(x+1, n)] 
    
    # 퀸의 대각선 (오른쪽 아래)
    while (x+1) in range(n) and (y+1) in range(n):
        result.append((x+1,y+1))
        x += 1
        y += 1 
    
    # x,y = position
    # 퀸의 대각선 (왼쪽 위)
    # while (x-1) in range(n) and (y-1) in range(n):
    #    result.append((x-1,y-1))
    #    x -= 1
    #    y -= 1 

    x,y = position
    # 퀸의 대각선 (왼쪽 아래)
    while (x+1) in range(n) and (y-1) in range(n):
        result.append((x+1,y-1))
        x += 1
        y -= 1 
    
    # x,y = position
    # 퀸의 대각선 (오른쪽 위)
    # while (x-1) in range(n) and (y+1) in range(n):
    #    result.append((x-1,y+1))
    #    x -= 1
    #    y += 1 

    return list(set(result))

def __help(pos, n, attacked, answer):
    x,y = pos
    
    # 마지막 행이면 
    if x == (n-1):
        return answer + 1
    
    # 다음 행 중 공격 범위에 없는 위치
    possible_pos = [(x+1, i) for i in range(n) if (x+1, i) not in attacked + attackRange(pos, n)]
    
    # 공격 범위에 없는 다음 행의 모든 위치들에 대해 
    for pp in possible_pos:
        answer = __help(pp, n, attacked + attackRange(pos, n), answer)
    
    # 공격 범위가 아닌 다음 행 위치가 없으면 
    if not possible_pos:
        return answer
    
    return answer
    

def solution(n):
    answer = 0

    for i in range(n//2):
        attacked = []
        # 첫 번째 퀸을 (0,0) ~ (0,n)까지 놓아보기 
        answer = __help((0,i), n, attacked, answer)
    

    # 짝수 (좌우대칭)
    if n % 2 == 0:
        return answer * 2 

    # 홀수 (좌우대칭 + 가운데)
    return answer * 2 + __help((0,n//2), n, [], 0)