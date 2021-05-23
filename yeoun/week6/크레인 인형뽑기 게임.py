def nonzero2list(tuples):
    result = []
    for t in tuples:
        if t != 0:
            result.append(t)
    # 위에 있는 인형이 더 끝에 오도록
    return result[::-1]

def solution(board, moves):
    # 터뜨러져 사라진 횟수
    answer = 0
    
    # 각 세로줄의 인형들 
    dolls_per_line = list(map(nonzero2list, zip(*board)))
    
    # 바구니
    basket = []
    for move in moves:
        dolls = dolls_per_line[move-1]
        # 인형이 있는 경우 
        if not dolls:
            continue 

        doll = dolls.pop()

        
        # 바구니가 비어있거나, 마지막으로 쌓인 인형이 현재 인형과 다른 경우 
        if basket == [] or basket[-1] != doll:
            # 바구니에 인형을 넣음 
            basket.append(doll)
        
        # 바구니의 마지막 인형이 현재 인형과 다른 경우 
        else:
            # 터뜨러져 사라진 횟수 + 1 
            answer += 1 
            basket.pop()
    
    # 터트러져 사라진 인형의 개수 = 터뜨러져 사라진 횟수 * 2 
    return answer * 2