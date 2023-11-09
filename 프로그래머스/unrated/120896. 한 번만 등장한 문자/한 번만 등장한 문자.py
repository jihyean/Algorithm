def solution(s):
    answer = ''
    str_set = set(list(s)) # 문자열 중복 제거
    str_list = list(str_set)
    
    for i in range(len(str_list)):                      # 문자 종류만큼 반복
        count = len(s)-len(s.replace(str_list[i], ''))  # 해당 문자가 포함된 개수

        if count <= 1: # 하나만 포함될 경우
            answer = answer + str_list[i]
    
    answer = ''.join(sorted(answer)) # 사전식 정렬
    
    return answer