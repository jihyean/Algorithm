def solution(num, total):
    answer = [] # n, n+1 , ..., n+num-1
    const = 0
    
    for i in range(num): # num만큼 반복
        const = const + i
        answer.append(i)
        
    n = (total - const) / num # (n * num) + 1 + 2 + ... + num-1 = total
    
    answer = list(map(lambda x:x +n, answer)) # 결과 리스트 각 원소에 n 더하기
    
    return answer