from itertools import combinations

def solution(numbers, target):
    answer = 0
    # 내림차순으로 정렬 
    numbers.sort(reverse = True)
    
    # number의 총 합 
    total = sum(numbers)
    
    # 총 합이 target과 같으면 모두 더하는 한 가지 방법만 가능 
    if total == target:
        return 1 
    
    # total > target 
    diff_half = int((total - target) / 2)
    
    # diff_half 이하인 값들만 저장 
    minus = []
    for i in range(len(numbers)):
        if numbers[i] <= diff_half:
            minus = numbers[i:]
            break
    
    # minus의 값들 중 합쳐서 혹은 그 자체로 diff_half가 되는 경우의 수  
    for i in range(1, len(minus)+1):
        combs = combinations(minus, i)
        for comb in combs:
            if sum(comb) == diff_half:
                answer += 1 
        
    return answer