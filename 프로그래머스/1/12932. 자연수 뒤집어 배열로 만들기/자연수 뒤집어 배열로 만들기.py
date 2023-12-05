def solution(n):
    answer = list(str(n))           # string 형변환 후 하나씩 잘라 저장
    answer.reverse()                # 역순
    answer = list(map(int, answer)) # 숫자로 변환
    
    return answer