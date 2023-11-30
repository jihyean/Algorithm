from functools import reduce

def solution(num_list):
    
    if(len(num_list) >= 11):                        # 리스트 길이가 11 이상인 경우
        answer = sum(num_list)                      # 리스트 모든 원소의 합
    else:                                           # 리스트 길이가 11 이상인 경우
        answer = reduce(lambda x,y : x*y, num_list) # 리스트 모든 원소의 곱
        
    return answer