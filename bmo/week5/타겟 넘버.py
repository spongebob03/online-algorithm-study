import itertools

def solution(numbers, target):
    answer = 0
    number = [(num, -num) for num in numbers]

    for combi in itertools.product(*number):
        if sum(combi) == target:
            answer += 1

    return answer