def is_valid(array, target, mid):
    return array[mid] >= target.replace('?', 'a') and array[mid] <= target.replace('?', 'z')

def binary_search1(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if is_valid(array, target, mid) and (mid == 0 or array[mid - 1] < target.replace('?', 'a')):
            return mid
        elif array[mid] >= target.replace('?', 'a'):
            end = mid - 1
        else:
            start = mid + 1
    return None

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if is_valid(array, target, mid) and (mid == len(array) - 1 or array[mid + 1] > target.replace('?', 'z')):
            return mid
        elif array[mid] > target.replace('?', 'z'):
            end = mid - 1
        else:
            start = mid + 1
    return None

def solution(words, queries):
    answer = []
    
    words.sort(key=lambda x: (len(x), x))
    arrays = [[] for _ in range(len(words[-1])+1)]
    
    for word in words:
        arrays[len(word)].append(word)

    for query in queries:
        n = len(query)
        array = arrays[n]
        target = query
        if query[0] == '?':
            array_r = []
            for array in arrays[n]:
                array_r.append(array[::-1])
            array_r.sort()
            array = array_r
            target = query[::-1]
        left = binary_search1(array, target, 0, len(array) - 1)
        right = binary_search2(array, target, 0, len(array) - 1)
        answer.append(right - left + 1) if (left, right) != (None, None) else answer.append(0)
    return answer

if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    print(solution(words, queries))