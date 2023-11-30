def solution(a, b, flag):
    answer = a - b      # 기본값 false로 설정
    
    if(flag):           # true일 경우
        answer = a + b  # a + b 할당
    return answer