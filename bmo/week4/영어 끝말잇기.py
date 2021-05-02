def solution(n, words):
    answer = [0, 0]
    history = set([words[0]])

    for idx in range(1, len(words)):
        if words[idx - 1][-1] == words[idx][0] and len(words[idx]) > 1 and words[idx] not in history:
            history.add(words[idx])
        else:
            answer = [idx % n + 1, idx // n + 1]
            break
    return answer