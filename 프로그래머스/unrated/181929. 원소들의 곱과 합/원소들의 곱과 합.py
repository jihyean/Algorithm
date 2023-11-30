from functools import reduce

def solution(num_list):
    answer = 0                                      # 기본값 0 설정
    num_sum = sum(num_list)                         # 모든 원소들의 합
    num_mul = reduce(lambda x,y : x*y, num_list)    # 모든 원소들의 곱
    
    if(num_mul < num_sum ** 2): # 모든 원소들의 곱이 더 작을 경우
        answer = 1
        
    return answer