def solution(num, k):
    num_str = str(num)              # 문자열로 변환
    answer = num_str.find(str(k))   # 문자열에서 k의 인덱스 찾기
    
    if answer != -1:        # k 존재시
        answer = answer + 1 # 인덱스가 아닌 자리이므로 +1
    
    return answer