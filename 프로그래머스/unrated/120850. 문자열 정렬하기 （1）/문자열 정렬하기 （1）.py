import re
def solution(my_string):
    
    my_string = re.sub(r'[^0-9]', '', my_string)    # 문자열에서 숫자만 남도록 함
    answer = list(map(int, my_string))              # 숫자 결과 리스트에 저장
    answer.sort()                                   # 결과 리스트 정렬
    
    return answer