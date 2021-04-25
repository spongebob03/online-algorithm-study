def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        prev_c = s[0:step]
        compressed = ''
        count = 1
        for j in range(step, len(s), step):
            curr_c = s[j: j+step]
            if prev_c == curr_c:
                count += 1
            else:
                compressed += str(count) + prev_c if count > 1 else prev_c 
                count = 1
                prev_c = curr_c
        compressed += str(count) + prev_c if count > 1 else prev_c
        answer = min(answer, len(compressed))
    return answer