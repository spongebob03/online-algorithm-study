def solution(n, s):
    if n > s: return [-1]

    answer = [s//n for _ in range(n)]

    for idx in range(s % n):
        answer[idx] += 1

    return sorted(answer)