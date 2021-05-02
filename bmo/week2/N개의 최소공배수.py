def getDivisor(number):
    divisor = dict()
    while number != 1:
        for i in range(2, number+1):
            if number % i == 0:
                divisor[i] = divisor.get(i, 0) + 1
                break
        number = number // i
    return divisor

def solution(arr):
    answer = 1
    divisor_union = dict()

    for divisors in [getDivisor(num) for num in arr]:
        for key, value in divisors.items():
            divisor_union[key] = max(divisor_union.get(key, 0), value)
    
    for key, value in divisor_union.items():
        answer *= key ** value

    return answer

if __name__ == '__main__':
    print(solution([2,6,8,14]))