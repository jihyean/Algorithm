def solution(angle):
    answer = 2                          # 기본값 직각
    
    if(angle < 90):                     # 90이하 예각일 경우
        answer = 1
    elif(angle > 90 and angle < 180):   # 90 ~ 180 사이 둔각일 경우
        answer = 3
    elif(angle == 180):                 # 180 평각일 경우
        answer = 4
    
    return answer