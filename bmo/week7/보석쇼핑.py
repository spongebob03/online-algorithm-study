def solution(gems):
    answer = []
    total = set(gems)
    n = len(total)

    for i in range(len(gems)-n):
        for j in range(i+n, len(gems)+1):
            curr = set(gems[i:j])
            
            if total.issubset(curr):
                answer.append((j-i, i+1, j))
    answer.sort()
    return [answer[0][1], answer[0][2]]