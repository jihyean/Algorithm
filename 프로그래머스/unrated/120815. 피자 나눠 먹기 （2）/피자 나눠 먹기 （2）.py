def solution(n):
    answer = 0  # 피자 판수
    pizza = 6   # 조각 수 = n과 6의 배수
    
    while (pizza % n != 0):
        pizza = pizza + 6
    
    answer = pizza / 6
    return answer