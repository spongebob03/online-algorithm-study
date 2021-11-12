import itertools

def solution(A, B):
    max_score = 0
    for combi in itertools.permutations(B):
        score = 0
        for a, b in zip(A, list(combi)):
            if b > a:
                score += 1
        max_score = max(max_score, score)
    
    return max_score

if __name__ == '__main__':
    result = solution([5,1,3,7], [2,2,6,8])
    print(result)