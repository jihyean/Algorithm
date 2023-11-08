def solution(n, t):
    answer = n # 처음 세균 수
    
    for i in range(t):      # t번 만큼 반복
        answer = answer * 2 # 두배만큼 증식
        
    return answer