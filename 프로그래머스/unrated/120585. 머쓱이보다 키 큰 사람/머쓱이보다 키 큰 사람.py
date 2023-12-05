def solution(array, height):
    answer = 0 # 키 큰 사람 수
    
    # 모든 사람의 수만큼 검사
    # 더 키가 크면 +1
    for i in array:
        if(i > height):
            answer = answer + 1

    return answer