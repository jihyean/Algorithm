def solution(n, k):
    service = n // 10               # 서비스로 받은 음료 개수
    k = k - service                 # 돈을 지불해야 하는 음료 개수
    answer = n * 12000 + k * 2000   # 총금액
    
    return answer