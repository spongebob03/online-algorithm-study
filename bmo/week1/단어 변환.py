def solution(begin, target, words):
    answer = 0
    stack = [begin]
    visited = {i:False for i in words}
    if target not in words:
        return 0

    while stack:
        current = stack.pop()
        if current == target:
            return answer
        
        for word in words:
            if not visited[word] and sum([x != y for x, y in zip(current, word)]) == 1:
                visited[word] = True
                stack.append(word)
                break
        answer += 1
    return answer

if __name__ == '__main__':
    result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
	)
    print(result)