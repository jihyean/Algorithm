def solution(money):
    answer = []
    
    answer.append(money//5500)  # 몫 == 최대로 마실 수 있는 아메리카노의 잔 수
    answer.append(money%5500)   # 나머지 == 잔돈
    
    return answer