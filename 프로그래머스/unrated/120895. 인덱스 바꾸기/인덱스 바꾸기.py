def solution(my_string, num1, num2):
    str_list = list(my_string) # 문자열 리스트로 변환
    
    # 주어진 정수에 따른 문자 순서 변경
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]
    
    answer = ''.join(str_list) # 리스트 문자열로 변환
    return answer