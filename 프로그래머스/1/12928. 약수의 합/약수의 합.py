def solution(n):
    answer = 0
    
    for i in range(1, n+1):     # 1부터 n까지 반복
        if(n % i == 0):         # 약수일 경우
            answer = answer + i # i 값 더하기
    return answer