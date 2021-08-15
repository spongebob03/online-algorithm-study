from collections import Counter

def solution(n, stages):
    answer = []
    Stage = Counter({_: 0 for _ in range(1, n+2)})
    Stage.update(stages)
    fail = {}

    for i in range(1, n+1):
        stop = Stage[i]
        success = stop
        for j in range(i+1, n+2):
            success += Stage[j]
        fail[i] = stop / success if stop != 0 else 0
        
    for key, _ in sorted(fail.items(), reverse=True, key=lambda x: x[1]):
        answer.append(key)

    return answer