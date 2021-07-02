from collections import defaultdict

# 이진 탐색 
def binary_search(array, suffix_idx, target, start, end, result):
    if start > end:
        return len(result) 

    mid = (start + end) // 2 

    # 중간값이 타겟인 경우 
    if array[mid][:suffix_idx] == target:
        # 현재 인덱스를 result 집합에 추가 
        result.add(mid)
        # 현재 인덱스보다 작은 쪽, 큰 쪽 모두 가보기 
        binary_search(array, suffix_idx, target, start, mid - 1, result)
        binary_search(array, suffix_idx, target, mid + 1, end, result)

    # 중간값이 타겟보다 큰 경우 
    elif target < array[mid][:suffix_idx]:
        binary_search(array, suffix_idx, target, start, mid - 1, result)

    # 중간값이 타겟보다 작은 경우 
    else:
        binary_search(array, suffix_idx, target, mid + 1, end, result)

    return len(result) 

def solution(words, queries):
    # key: 단어 길이, value: 해당 길이의 단어들 
    word_dict = defaultdict(list)
    # key: 단어 길이, value: 해당 길이의 단어들의 앞뒤를 뒤집은 형태 
    reversed_word_dict = defaultdict(list)
    for word in words:
        word_dict[len(word)].append(word)
        reversed_word_dict[len(word)].append(word[::-1])

    # value를 알파벳 순으로 정렬 
    word_dict = {key: sorted(words) for key, words in word_dict.items()}
    reversed_word_dict = {key: sorted(words) for key, words in reversed_word_dict.items()}
    
    matching_dict = defaultdict(int)
    
    for q in set(queries):
        # query가 ?로만 이루어진 경우 
        if set(q) == set('?'):
            if len(q) not in word_dict:
                matching_dict[q] = 0
                continue        
            matching_dict[q] = len(word_dict[len(q)])
            
        # query의 접미사가 ?인 경우 
        elif not q.startswith('?'):
            if len(q) not in word_dict:
                matching_dict[q] = 0
                continue 
            array = word_dict[len(q)]
            suffix_idx = q.index('?')
            target = q[:suffix_idx]
            matching_dict[q] = binary_search(array, suffix_idx, target, 0, len(array)-1, result=set())
            
        # query의 접두사가 ?인 경우 
        # query의 앞뒤를 뒤집어 접미사인 경우와 동일하게 탐색 
        else:
            if len(q) not in reversed_word_dict:
                matching_dict[q] = 0
                continue 
            array = reversed_word_dict[len(q)]
            prefix_idx = q[::-1].index('?')
            target = q[::-1][:prefix_idx]
            matching_dict[q] = binary_search(array, prefix_idx, target, 0, len(array)-1, result=set())
    
    # 중복된 query가 있을 수 있으므로 
    answer = []
    for query in queries:
        answer.append(matching_dict[query])
    return answer