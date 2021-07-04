import re
from collections import defaultdict

def solution(words, queries):
    queries = [query.replace('?', '.') for query in queries]
    words.sort(key=lambda x: len(x))
    
    matching_dict = defaultdict(int)
    
    for q in set(queries):
        for word in words:
            if len(word) == len(q):
                result = re.match(q, word)
                if result:
                    matching_dict[q] += 1 
            elif len(word) > len(q):
                break
    
    answer = []
    for query in queries:
        answer.append(matching_dict[query])
    return answer