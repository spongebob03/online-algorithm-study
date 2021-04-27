def valid(s):
    stack = []
    bracket = {
        ']' : '[',
        '}' : '{',
        ')' : '('
    }
    
    for c in s:
        if c in bracket.values():
            stack.append(c)
        else:
            if stack and stack[-1] == bracket[c]:
                stack.pop()
            else:
                return False
    return True if not stack else False

def solution(s):
    answer = 0

    for x in range(len(s)):
        brackets = s[x:] + s[:x]
        if valid(brackets):
            answer += 1

    return answer