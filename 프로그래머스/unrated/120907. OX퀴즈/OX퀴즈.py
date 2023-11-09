def solution(quiz):
    answer = []
    
    for i in range(len(quiz)):              # quiz 길이만큼 반복
        equation = quiz[i].split(' ', 3)    # 공백 기준으로 x, y, z, 연산자 추출
        x = int(equation[0])
        operator = equation[1]
        y = int(equation[2])
        z = int(equation[3].replace('= ', '')) # '= ' 제거
        
        if(operator == '+'):    # 연산자가 '+' 일때
            result = x + y
        else:                   # 연산자가 '-' 일때
            result = x - y

        if result == z:         # 수식이 옳았을 경우
            answer.append('O')
        else:                   # 수식이 틀렸을 경우   
            answer.append('X')

    return answer