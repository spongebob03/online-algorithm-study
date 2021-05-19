def solution(n, a, b):
    answer = 1
    while True:
        if abs(a - b) == 1 and max(a, b) % 2 == 0:
            break
        a = a // 2 if a % 2 == 0 else (a // 2) + 1
        b = b // 2 if b % 2 == 0 else (b // 2) + 1
        answer += 1

    return answer