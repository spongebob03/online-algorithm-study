def next_stage(num):
    return num //2 if num % 2 == 0 else (num // 2) + 1

def solution(n, a, b):
    answer = 1
    while True:
        if abs(a - b) == 1 and max(a, b) % 2 == 0:
            break
        a = next_stage(a)
        b = next_stage(b)
        answer += 1

    return answer