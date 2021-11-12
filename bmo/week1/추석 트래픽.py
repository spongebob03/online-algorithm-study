def StartEndSec(line):
    date, time, T = line.split()
    h, m, s = time.split(':')    
    end = int(h) * 60 * 60 + int(m) * 60 + float(s)
    T = float(T[:-1])
    return end - T + 0.001 - 0.9991, end

def duplicateCheck(sec, time_table):
    if sec not in time_table.keys():
        return sec
    else:
        return dup(sec - 0.0000001)

def solution(lines):
    time_table = dict()

    for idx, line in enumerate(lines):
        for sec in StartEndSec(line):
            sec = duplicateCheck(sec, time_table)
            time_table[sec] = idx
    
    history = []
    state = [False] * len(lines)

    for time in sorted(time_table.keys()):
        idx = time_table[time]
        # 트래픽 on, off
        state[idx] = not state[idx]
        # 활성화된 트래픽 개수 기록
        history.append(state.count(True))
    
    return max(history)


if __name__ == '__main__':
    lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    result = solution(lines)
    print(result)