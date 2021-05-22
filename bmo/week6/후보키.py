import itertools

def solution(relation):
    n = len(relation[0])
    keys = set()

    for i in range(1, n+1):
        for combi in itertools.combinations([i for i in range(n)], i):
            records = set()
            for rel in relation:
                record = ''
                for col in combi:
                    record += rel[col]
                records.add(record)

            # 식별자가 된 경우 후보키 여부 판별
            if len(records) == len(relation):
                for key in keys:
                    if not set(key) - set(combi):
                        break
                else:
                    keys.add(combi)
                    
    return len(keys)      