def solution(s):
    flag_plus = True
    
    # 부호가 있을 경우 제거 후 양수 여부 저장
    if(s[0] == '-'):
        s = s[1:]
        flag_plus = False
    elif(s[0] == '+'):
        s = s[1:]
    
    answer = int(s) # 문자열 형변환
    
    if(not flag_plus): # 음수일 경우 변환
        answer = -answer  
    
    return answer