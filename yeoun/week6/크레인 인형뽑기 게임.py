def solution(board, moves):
    # 터뜨러져 사라진 횟수
    answer = 0
    
    # 각 세로줄의 인형들 
    transposed_board = list(map(list, zip(*board)))
    
    # 바구니
    basket = []
    for move in moves:
        for idx, element in enumerate(transposed_board[move-1]):
            # 인형이 있는 경우 
            if element != 0:
                # 현재 칸의 값을 인형으로 저장 
                doll = element
                # 인형이 꺼내진 것이므로 빈 칸을 의미라는 0으로 수정
                transposed_board[move-1][idx] = 0
                break
                
        # break로 for문을 빠져나오지 않은 경우
        # 즉, 해당 세로줄에 인형이 없는 경우 
        else:
            continue
        
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