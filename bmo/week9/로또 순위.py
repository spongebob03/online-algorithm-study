def solution(lottos, win_nums):
    zeros = lottos.count(0)
    correct = len(set(lottos) & set(win_nums))
    
    best = 7 - (correct + zeros) if correct > 0 or zeros > 0 else 6
    worst = 7 - correct if correct > 0 else 6

    return [best, worst]