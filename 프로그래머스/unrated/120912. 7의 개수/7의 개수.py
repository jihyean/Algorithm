def solution(array):
    
    arrStr = ''.join(map(str, array)) # 리스트를 하나의 문자열로 변환
    answer = len(arrStr) - len(arrStr.replace('7','')) # 문자열에 포함된 7의 개수
    
    return answer