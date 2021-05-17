def ngram(s, n):
    result = ''
    prev = ''
    digit = 0 
    
    for i in range(0,len(s),n):
        cur = s[i:i+n]
        # 이전과 같다면 count 하나씩 올려주기 
        if prev == cur:
            count = int(result[-digit:])
            result =  result[:-digit] + str(count + 1)
            #9, 99, 999,...이면 자릿수 1 증가 
            if set(str(count)) == {'9'}:
                digit += 1 
        # 이전과 다르다면 현재 ngram과 빈도 1을 더해주기 
        else:
            # 직전의 ngram 빈도가 1인 경우, 1 지우기 
            if digit == 1 and result.endswith('1'):
                result = result[:-1]
            result += cur + '1' 
            digit = 1 
        # 이전 ngram을 현재의 것으로 업데이트 
        prev = cur
    
    # 마지막 ngram 빈도가 1인 경우, 1 지우기
    if digit == 1 and result.endswith('1'):
        result = result[:-1]
    return result


def solution(s):
    length = len(s)
    min_length = length
    
    # 각 i개 단위로 잘라 압축했을 때, 최단 길이 반환하기 
    for i in range(1, length):
        cur_length = len(ngram(s, i))
        if min_length > cur_length:
            min_length = cur_length
    
    return min_length