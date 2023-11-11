def solution(slice, n):
    answer = 1  # 피자 판수
    
    while( slice * answer ) < n: # 전체 조각 수가 사람수보다 커질 때까지
        answer = answer + 1
    
    return answer