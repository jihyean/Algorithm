def solution(n):
    answer = 0  # 총합

    # n까지 반복
    # 짝수일 경우 해당 값 합산
    for i in range(n+1):
        if(i % 2 == 0): 
            answer = answer + i

    return answer