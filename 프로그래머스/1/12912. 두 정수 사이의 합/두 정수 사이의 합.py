def solution(a, b):
    answer = 0
    flag = True
    
    if(a > b):
        a, b = b, a
    elif(a == b):
        answer = a
        flag = False

    if(flag):
        for i in range(a,b+1):
            answer = answer + i

    return answer