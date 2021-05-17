def __help(tickets, answer, candidates):
    
    for i, ticket in enumerate(tickets):
        # 마지막 방문 공항(answer[-1])과 이번 티켓의 출발 공항(ticket[0])이 같으면
        if ticket[0] == answer[-1]:    
            # 현재 티켓을 제외한 tickets, 현재 티켓의 도착 공항을 더해준 answer, candidate
            __help(tickets[:i] + tickets[i+1:], answer + [ticket[1]], candidates)
    
    # 모든 티켓을 사용한 경우 
    if not tickets:
        candidates.append(answer)
        
    return candidates

def solution(tickets):
    answer = ['ICN']
    # 모든 티켓을 사용할 수 있는 경로 
    candidates = []
    
    candidates = __help(tickets, answer, candidates)
    
    # candidate 중에서 알파벳 순서가 가장 앞서는 경로 
    return sorted(candidates)[0]
    