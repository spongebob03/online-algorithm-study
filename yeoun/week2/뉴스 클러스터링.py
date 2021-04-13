from collections import Counter
import math

def getBigram(string):
    bigrams = []
    for i in range(len(string)-1):
        # 두 문자씩 bigram 만들기 
        bigram = string[i:i+2]
        # 만들어진 bigram이 알파벳으로만 이루어진 경우 리스트에 추가 
        if bigram.isalpha():
            bigrams.append(bigram)
    return bigrams

def solution(str1, str2):
    # 대소문자를 구별하지 않으므로 소문자로 통일 
    str1 = str1.lower()
    bigram1 = getBigram(str1)
    
    str2 = str2.lower()
    bigram2 = getBigram(str2)
    
    # 중복을 포함한 교집합 
    intersection = list((Counter(bigram1) & Counter(bigram2)).elements())
    # 중복을 포함한 합집합 
    union = list((Counter(bigram1) | Counter(bigram2)).elements())
    
    # 분모가 0인 경우 점수를 1로 
    if len(union) == 0:
        score = 1
    else:
        score = (len(intersection) / len(union)) 

    # 소수점 버림 
    return math.trunc(score * 65536)