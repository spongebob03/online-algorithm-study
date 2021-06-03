# 참고: https://wwlee94.github.io/category/algorithm/binary-search/immigration/

def solution(n, times):
    answer = 0
    # 심사에 걸리는 최소 시간 
    min_time = 1
    # 심사에 걸리는 최대 시간: 가장 오래 걸리는 심사대에서 모두가 심사 받는 경우 
    max_time = max(times) * n 
    
    while min_time <= max_time:
        # 중간값 
        mid = (min_time + max_time) // 2 
        # 심사시간이 중간값일 때, 심사할 수 있는 사람의 수 
        count = 0
        for time in times:
            count += mid // time
            if count >= n:
                break
        
        # n명 이상 심사할 수 있는 경우: 심시시간 줄여보기 
        if count >= n:
            answer = mid
            max_time = mid - 1 
        # n명을 모두 심사할 수 없는 경우: 심사시간 늘려보기 
        else:
            min_time = mid + 1
            
        
    return answer 