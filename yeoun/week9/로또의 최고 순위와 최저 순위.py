from collections import Counter

def solution(lottos, win_nums):
    # key: 일치한 숫자의 개수, value: 순위
    num2rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    # 겹치는 숫자의 개수 
    sames = len(set(lottos) & set(win_nums))
    # 알아볼 수 없는 숫자의 개수 
    zeros = Counter(lottos)[0]
    
    # 알아볼 수 없는 숫자가 모두 당첨번호와 일치하는 경우 
    best = sames + zeros
    # 알아볼 수 없는 숫자 중 아무것도 당첨번호와 일치하지 않는 경우 
    worst = sames 
    
    return [num2rank[best], num2rank[worst]]