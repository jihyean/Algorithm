def solution(n, numlist):
    answer = []
    
    for i in range(len(numlist)):       # numlist 길이만큼 반복
        if (numlist[i] % n) == 0:       # numlist의 배수일 경우
            answer.append(numlist[i])   # 결과 리스트에 저장
    
    return answer