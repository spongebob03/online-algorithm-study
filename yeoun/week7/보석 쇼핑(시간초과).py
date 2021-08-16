from itertools import combinations

def solution(gems):
    # 진열대 길이 
    N = len(gems)
    # 보석의 종류들 
    gem_types = set(gems)
    
    # 보석이 한 종류면 첫번째 것만 고르면 됨 
    if len(gem_types) == 1:
        return [1,1]
    
    # 선택의 시작과 끝을 combination으로 구함 
    combs = list(combinations(list(range(N)), 2))
    
    # 진열대 총 길이로 span 초기화 
    span = N
    
    # 선택의 시작 번호가 큰 것에서 작은 것으로 순서대로 
    for comb in combs[::-1]:
        # 현재 고른 시작과 끝에 모든 보석의 종류가 포함되어 있으면 
        if set(gems[comb[0]:comb[1]+1]) == gem_types:
            cur_span = comb[1] - comb[0] + 1 
            # 현재 span이 지금까지의 span보다 작으면 (더 짧은 구간이면)
            if cur_span <= span:
                span = cur_span 
                # 진열대 번호는 0이 아니라, 1부터 시작하므로 
                answer = [comb[0]+1, comb[1]+1]
                
    return answer