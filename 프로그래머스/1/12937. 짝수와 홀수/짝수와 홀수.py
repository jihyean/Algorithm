def solution(num):
    answer = 'Even' # 기본값 짝수 'Even' 설정
    
    if(num % 2 != 0): # 홀수일 경우
        answer = 'Odd'
    
    return answer