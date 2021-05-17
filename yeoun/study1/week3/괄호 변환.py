# 균형잡힌 괄호 문자열: '(' 의 개수와 ')' 의 개수가 같음 
def balanced(p:str) -> bool:
    return p.count('(') == p.count(')')

# 올바른 괄호 문자열: 균형잡혔으며 '('와 ')'의 괄호의 짝도 모두 맞음 
def correct(p:str) -> bool:
    if not balanced(p) or p.startswith(')') or p.endswith('('):
        return False
    else:
    	stack = []
    	for element in p:
    		if element == ')' and stack:
    			stack.pop()
    		else:
    			stack.append(element)

    return True if not stack else False

# 문자열의 괄호 방향 뒤집기 
def flip(p:str) -> str:
    result = ''
    for element in p:
        if element == '(':
            result += ')'
        else:
            result += '('
    return result
    
    
def solution(p:str) -> str:
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == '':
        return p

    for i in range(2, len(p)+1, 2):
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        if balanced(p[0:i]):
            u = p[0:i]
            v = p[i:]
            break
    
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if correct(u):
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return u + solution(v)
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        # 4-3. ')'를 다시 붙입니다. 
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        # 4-5. 생성된 문자열을 반환합니다.
        return '(' + solution(v) + ')' + flip(u[1:-1])
