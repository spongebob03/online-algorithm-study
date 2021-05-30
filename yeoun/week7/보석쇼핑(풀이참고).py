from collections import defaultdict 

def solution(gems):
    # [key] 보석이름, [value] 보석 개수 
    gem_dict = defaultdict(int)
    # left, right 모두 0인 경우를 기준으로 gem_dict 값 초기화 
    # 첫 번째 보석만 한 개 포함된 상태 
    gem_dict[gems[0]] = 1
    # 전체 보석 개수 
    N = len(set(gems))
    
    span = len(gems) + 1
    left, right = 0, 0
    
    while True:
        # 진열대 index 넘어가면 반복문 탈출 
        if left < 0 or right > len(gems)-1:
            break
        
        # 모든 보석이 포함된 경우 
        if len(gem_dict) == N:
            # 구간의 길이가 짧은 경우 
            if right - left + 1 < span:
                # 진열대 번호가 0이 아닌, 1부터 시작하므로 
                answer = [left+1, right+1]
                span = right - left + 1
            # 왼쪽 포인터 1만큼 증가 
            left += 1 
            # 그에 따라 없어지는 보석 개수 업데이트 
            gem_dict[gems[left-1]] -= 1 
            # 이때 특정 보석이 0개가 된 경우 딕셔너리에서 삭제 
            if gem_dict[gems[left-1]] == 0:
                gem_dict.pop(gems[left-1])
                
        # 모든 보석이 포함되지 않은 경우
        else:
            # 오른쪽 포인터 1만큼 증가 
            right += 1 
            # 증가해도 아직 진열대 안에 있다면 
            if right < len(gems):
                # 새로 포함된 보석 빈도수 1만큼 증가 
                gem_dict[gems[right]] += 1 

    return answer