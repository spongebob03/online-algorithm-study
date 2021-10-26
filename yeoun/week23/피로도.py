from itertools import permutations

# 주어진 순서에 따라 방문할 수 있는 던전의 수 
def count_dungeoun(k, dungeons):
    result = 0
    for dungeon in dungeons:
        need, minus = dungeon
        if k < need:
            return result
        k -= minus
        result += 1
    return result

def solution(k, dungeons):
    # 모든 가능한 순서로 섞기 
    shuffled = permutations(dungeons, len(dungeons))
    answers = []
    for s in shuffled:
        answers.append(count_dungeoun(k, s))
    
    return max(answers)