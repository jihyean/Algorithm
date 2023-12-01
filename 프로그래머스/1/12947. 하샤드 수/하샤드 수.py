def solution(x):
    answer = False  # 기본값 Flase 지정
    
    N=[int(i) for i in str(x)]  # 문자열로 변환하여 하나씩 잘라 배열에 저장
    
    if(x % sum(N) == 0):        # x 가 자리수의 합으로 나누어 떨어질 경우
        answer = True           # True 할당
    
    return answer