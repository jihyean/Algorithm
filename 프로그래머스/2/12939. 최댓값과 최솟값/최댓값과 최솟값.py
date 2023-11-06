def solution(s):
    answer = ''
    strarr = s.split(' ') # 공백 단위로 잘라 리스트에 저장
    
    intarr = list(map(int, strarr)) # 리스트에 저장된 변수 타입을 int 타입으로 변환
    answer = str(min(intarr)) + ' ' +str(max(intarr)) #최소값과 최대값 저장
    
    return answer