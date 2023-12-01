def solution(s):
    answer = True # 기본값 True 지정
    
    s = s.upper()           # 문자열 전부 대문자로 변환
    cnt_p = s.count('P')    # 'P' 개수 카운트
    cnt_y = s.count('Y')    # 'Y' 개수 카운트
    
    if(cnt_p != cnt_y): # 'P'와 'Y'의 개수가 다를 경우
        answer = False  # False 할당
        
    return answer