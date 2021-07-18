def solution(words, queries):
    answer = []
    for query in queries:
        count = 0
        for word in words:
            keyword = True
            if len(query) == len(word):
                for i in range(len(query)):
                    if query[i] != word[i] and query[i] != '?':
                        keyword = False
            else:
                keyword = False

            if keyword:
                count += 1

        answer.append(count)
    
    return answer

if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]	
    print(solution(words, queries))