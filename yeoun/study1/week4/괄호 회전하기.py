def is_correct(s):
    parenthesis = {')':'(', '}':'{', ']':'['}
    
    # 첫 시작이 닫는 괄호면 False 
    if s[0] in parenthesis.keys():
        return False

    # 첫 시작이 여는 괄호인 경우 
    stack = []
    for element in s:
        # 닫는 괄호고 stack에 pop할 것이 있는 경우 
        if element in parenthesis.keys() and stack:
            if parenthesis[element] != stack.pop():
                return False
        # 여는 괄호 또는 stack이 비어있는 경우 
        else:
            stack.append(element)
    # stack이 비어 있으면 True, 아니면 False 
    return True if not stack else False

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        # 0 ~ len(s)-1 까지 회전시키기 
        if is_correct(s[i:] + s[:i]):
            answer += 1 

    return answer