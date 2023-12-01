def solution(x, n):
    answer = []
    
    # n번 만큼 반복
    for i in range(n): 
        answer.append((i+1)*x) # (인덱스+1) * x
    return answer