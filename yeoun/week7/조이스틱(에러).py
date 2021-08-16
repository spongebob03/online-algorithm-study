import re 

def minMove(name):

    spanA = [(m.start(0), m.end(0)) for m in re.finditer('A{1,}', name)]
    
    # A가 없는 경우 
    if not spanA:
        return len(name) - 1 
    
    maxSpanLength = max([s[1]-s[0] for s in spanA])
    maxSpanA = [s for s in spanA if s[1]-s[0] == maxSpanLength][-1]
    # 가장 길게 연속적으로 A가 있는 부분의 시작과 끝 index 
    ignore_start, ignore_end = maxSpanA 
    
    # 가장 긴 A의 연속체가 처음부터 있으면
    # 처음부터 왼쪽으로만 
    if ignore_start == 0:
        return len(name) - (ignore_end)
    
    # 가장 긴 A의 연속체가 끝부분에 있으면
    # 처음부터 오른쪽으로 가고, 가장 긴 A의 연속체가 시작되기 직전까지만 커서 이동 
    elif ignore_end == len(name):
        return ignore_start - 1
    
    # 중간에 가장 긴 A의 연속체가 있으면 
    # 연속체의 왼쪽, 오른쪽 길이 비교해서 더 짧은 곳 먼저 가고 다시 돌아와서 나머지 부분으로 커서 이동 
    else:
        left = ignore_start - 1
        right = len(name) - (ignore_end)
        
        if left > right:
            return right * 2 + left
        else:
            return left * 2 + right    
    
def solution(name):
    
    # 커서 이동에 필요한 조작 횟수 
    answer = minMove(name)
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # A에서 위로 조작하는 것이 더 빠른 알파벳들 
    ups = alphabet[:len(alphabet)//2]
    # A에서 아래로 조작하는 것이 더 빠른 알파벳들 (N은 똑같이 13번이긴 함)
    downs = alphabet[len(alphabet)//2:]
    
    # 이동빼고 철자 만드는데 필요한 조작횟수
    for n in name:
        if n == 'A':
            continue
        else:
            if n in ups:
                answer += alphabet.index(n)
            else:
                answer += len(alphabet) - alphabet.index(n)
    
    return answer