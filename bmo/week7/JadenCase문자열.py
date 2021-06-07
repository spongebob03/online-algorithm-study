def solution(s):
    answer = ""
    space = True

    for c in s:
        if c == ' ':
            answer += c
            space = True
        elif space:
            answer += c.upper()
            space = False
        else:
            answer += c.lower()

    return answer