# query와 key가 한 알파벳만 다른 사이면 True, 아니면 False 
def checkdiff1(query, key):
    diff = 0
    for a,b in zip(query,key):
        if a != b:
            diff += 1 
    return diff == 1 

def solution(begin, target, words):
    answer = []
    
    # words에 target 단어가 없으면 begin을 target으로 반환할 수 없으므로 0 반환 
    if target not in words:
        return 0

    # target에서 한 알파벳씩만 바꾸면서 begin으로 갈 수 있는지 확인 
    def search(target, words, depth):
        for word in words:
            # target 단어 자체가 한 알파벳만 바꾸면 begin이 되는 경우 
            if word == target and checkdiff1(begin, word):
                # 현재 depth를 answer에 추가 
                answer.append(depth)
            # words 안의 단어 중 target과 한 알파벳만 다른 사이인 경우 
            elif checkdiff1(target, word):
                # depth를 하나 더 늘려서 target 제외한 words 리스트에서 한 알파벳만 다른 사이들을 다시 search 
                search(word, [w for w in words if w != target], depth+1) 
        
    search(target, words, 1)
    
    # answer의 값 중 최솟값을 반환 
    return min(answer)