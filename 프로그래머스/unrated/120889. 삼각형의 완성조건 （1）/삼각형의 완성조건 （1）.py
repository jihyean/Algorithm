def solution(sides):
    answer = 2
    sides.sort() # 선분 길이 순 정렬
    
    if(sides[0] + sides[1] > sides[2]): # 삼각형을 만들 수 있을 경우
        answer = 1
    
    return answer