def solution(array):
    answer = []
    
    answer.append(max(array)) # 최대값 저장
    answer.append(array.index(answer[0])) # 최대값의 인덱스 저장

    return answer