from collections import deque

def solution(skill, skill_trees):
    answer = 0
    skill_order = {skill: idx for idx, skill in enumerate(skill)}
    
    for skill_tree in skill_trees:
        skill_tree = deque(skill_tree)
        master = -1
        success = True

        while skill_tree:
            curr_skill = skill_order.get(skill_tree.popleft(), -1)

            # 이미 습득한 스킬이거나 마스터 스킬의 바로 다음 스킬이라면
            if curr_skill <= master or curr_skill - master == 1:
                if curr_skill - master == 1:
                    master = curr_skill
            else:
                success = False
                break
        if success:
            answer += 1

    return answer