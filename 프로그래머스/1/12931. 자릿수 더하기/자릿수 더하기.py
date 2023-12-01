def solution(n):
    N = [int(i) for i in str(n)] # 각 자리수를 잘라 배열에 저장
    
    answer = sum(N) # 각 자리수의 합

    return answer