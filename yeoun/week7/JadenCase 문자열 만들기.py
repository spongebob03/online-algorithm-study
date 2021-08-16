import re 

def solution(s):
    answer = ''
    # 단어를 구분하는 공백들을 리스트로 
    # word의 개수와 똑같이 맞추기 위해 빈 문자열을 맨 뒤에 추가 
    seps = re.findall('\s{1,}', s) + ['']
    
    for word, sep in zip(s.split(), seps):
        # 첫 문자만 대문자, 나머지는 소문자로 변환하고 해당 공백을 더함 
        answer += word[0].upper() + word[1:].lower() + sep
        
    return answer