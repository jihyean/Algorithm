def solution(my_str, n):
    answer = []
    
    for i in range(len(my_str)//n): # 문자열 길이를 n과 나눈 몫만큼 반복
        answer.append(my_str[0:n])  # 결과 리스트에 n만큼 잘라서 추가
        my_str = my_str.replace(answer[i], '', 1) # 추가한 만큼 제거
    
    if(len(my_str)>0): # 남아있는 문자열이 있을시 마지막에 추가
        answer.append(my_str)
    
    return answer