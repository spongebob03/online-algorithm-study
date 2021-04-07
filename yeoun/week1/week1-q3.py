def solution(skill, skill_trees):
    answer = 0
    
    # 주어진 skill에서 가능한 순서 
    # ex) skill = "CBD"인 경우, valid = ['', 'C', 'CB', 'CBD']
    valid = [skill]
    for i in range(len(skill)):
        valid.append(skill[:i])
    
    # 각 skill_tree에 대해 
    for skill_tree in skill_trees:
    	# 주어진 skill에 포함되지 않은 스킬은 지운 상태가 valid에 포함되는 지 확인 
    	# ex) skill_tree = "BACDE"인 경우, "BCD"가 valid 안에 있지 않으므로 answer는 증가하지 않음 
        if ''.join([s for s in skill_tree if s in skill]) in valid:
            answer += 1
            
    return answer 