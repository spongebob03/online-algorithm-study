import re 

def ngram(s, n):
    result = ''
    prev = ''
    
    for i in range(0,len(s),n):
        cur = s[i:i+n]
        # 이전과 같다면 count 하나씩 올려주기 
        if prev == cur:
            idx = -1
            # 마지막 숫자의 자릿수 확인 
            while len(result) > -idx and result[idx].isdigit():
                idx -= 1 
            result =  result[:idx+1] + str(int(result[idx+1:]) + 1)
        # 이전과 다르다면 현재 ngram과 빈도 1을 더해주기 
        else:
            result += cur + '1' 
        # 이전 ngram을 현재의 것으로 업데이트 
        prev = cur
    
    # 맨 마지막 ngram 빈도가 1인 경우, 1 지우기 
    if result[-2].isalpha() and result[-1] == '1':
        result = result[:-1]
    # 알파벳 사이에 있는 1은 모두 지우기 
    return re.sub('(?<=[a-z])1(?=[a-z])', '', result) 


def solution(s):
    length = len(s)
    min_length = length
    
    # 각 i개 단위로 잘라 압축했을 때, 최단 길이 반환하기 
    for i in range(1, length):
        cur_length = len(ngram(s, i))
        if min_length > cur_length:
            min_length = cur_length
    
    return min_length