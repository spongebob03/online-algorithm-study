import itertools

def solution(n, s):
    answer = []
    numbers = [_ for _ in range(1, s)]
    combis = set()

    for combi in itertools.combinations(numbers, n):
        if sum(combi) == s:
            combis.add((combi[0] * combi[1], combi))
    if s % 2 == 0: combis.add(((s//2)**2, (s//2, s//2)))
    
    if not combis: return [-1]
    for number in sorted(list(combis), reverse= True)[0][1]:
        answer.append(number)
    
    return answer

if __name__ == '__main__':
    result = solution(2, 8)
    print(result)