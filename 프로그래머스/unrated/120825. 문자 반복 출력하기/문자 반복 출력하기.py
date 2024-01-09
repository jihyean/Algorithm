def solution(my_string, n):
    answer = ''

    for i in my_string:
        for k in range(n):
            answer = answer + i
    
    return answer