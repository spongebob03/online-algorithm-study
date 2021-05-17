def solution(A, B):
    answer = 0
    
    for a in A:
        # 현재 a의 값보다 큰 b 값들 
        largerB = [b for b in B if a < b]
        if not largerB: # empty list
            continue 
        else:
            # 그 중의 최솟값 선택 
            selected_a = min(largerB)
            # 선택된 최솟값은 다시 선택될 수 없으므로 제거 
            B.remove(selected_a)
            # 한 번 이긴 것이므로 answer + 1 증가 
            answer += 1 
    
    return answer