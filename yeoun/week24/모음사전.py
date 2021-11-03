vowels = ['A','E','I','O','U']
orders = {'A':1,'E':782,'I':1563, 'O':2344, 'U':3125}

def find_order(word):
    if len(word) < 2:
        return orders[word]
    blanks = 5 - len(word)
    # ex) EIO는 EIIUU 바로 다음이므로 
    if word[-1] != 'A': # 무한루프 방지 
        return find_order(word[:-1] + vowels[vowels.index(word[-1])-1] + 'U'*(blanks)) + 1
    # ex) EIA는 EI 바로 다음이므로 
    return find_order(word[:-1]) + 1
    
def solution(word):
    if word in orders:
        return orders[word]
    return find_order(word)