def solution(num, n):
    answer = 0          # 배수가 아닐시 0 기본값 설정
    
    if(num % n == 0):   # 배수일시 1 설정
        answer = 1
    
    return answer