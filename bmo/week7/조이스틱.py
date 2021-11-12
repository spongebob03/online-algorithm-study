def solution(name):
    answer = 0
    gaps = []
    for c in name:
        gap = ord(c) - ord('A') if ord(c) - ord('A') < 13 else ord('Z') - ord(c) + 1
        gaps.append(gap)
    
    answer = sum(gaps)
    skip = 0

    for i in range(len(gaps)):
        print(gaps[i])
        if gaps[i] == 0:
            skip += 1
        else:
            if i > 1:
                break

    answer += len(gaps) - skip - 1
    return answer

if __name__ == '__main__':
    solution("ZZAAAZZ") # 이 경우, 왔던 칸으로 돌아가는 것이 더 빠르다