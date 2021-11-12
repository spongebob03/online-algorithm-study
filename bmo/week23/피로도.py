import itertools

def solution(k, dungeons):
    answer = 0
    for order in itertools.permutations(dungeons):
        hp = k
        count = 0
        for rq, cost in order:
            if hp >= rq:
                count += 1
                hp -= cost
        answer = max(answer, count)
    return answer

if __name__ == '__main__':
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution(k, dungeons))