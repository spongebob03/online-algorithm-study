from collections import deque 

def solution(s):

    q = deque()
    
    for char in s:
        # 큐가 비어있거나 마지막 요소가 현재 문자와 다르면, 현재 문자 추가
        if not q or q[-1] != char:
            q.append(char)
        # 큐의 마지막 요소와 현재 문자가 같으면, 마지막 요소 제거 
        else:
            q.pop()
    
    # 큐가 비어 있으면 문자열을 모두 제거한 것이므로 1 반환 
    if not q:
        return 1
    else:
        return 0
