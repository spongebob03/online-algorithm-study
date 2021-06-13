def is_balance(s):
    return s.count('(') == s.count(')')

def is_valid(s):
    stack = []
    for blacket in s:
        if blacket == ')' and stack:
            stack.pop()
        else:
            stack.append(blacket)
    return True if not stack else False

def reverse_blacket(s):
    reverse_s = ''
    for blacket in s:
        if blacket == ')':
            reverse_s += '('
        else:
            reverse_s += ')'
    return reverse_s

def solution(w):
    if not w: return w
    u = ''
    v = ''
    for i in range(len(w), -1, -1):
        u = w[0:i]
        if is_balance(u):
            v = w[i:-1]
            break
    answer = ''
    if is_valid(u):
        return u + solution(v)
    else:
        answer += '(' + solution(v) + ')' + reverse_blacket(u[1:-1])
        return answer