def solution(n, words):

    for i in range(1, len(words)):
        # (1) 끝말이 이어지지 않는 경우 (2) 한글자인 단어를 말하는 경우 (3) 이전에 등장한 단어를 사용하는 경우 -> 끝말잇기 실패 
        if words[i][0] != words[i-1][-1] or len(words[i]) == 1 or words[i] in words[:i]:    
            # 번호: i를 n으로 나눈 나머지 +1 
            # 차례: i를 n으로 나눈 몫 + 1 
            return [i%n+1, i//n+1]

    return [0,0]