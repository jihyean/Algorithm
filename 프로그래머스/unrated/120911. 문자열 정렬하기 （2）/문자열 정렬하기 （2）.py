def solution(my_string):
    str_list = list(my_string.lower())  # 문자열을 소문자로 변환 뒤 리스트에 나눠 저장
    str_list.sort()                     # 알파벳 순서대로 정렬
    
    answer = ''.join(str_list)          # 리스트를 하나의 문자열로 변환
                     
    return answer