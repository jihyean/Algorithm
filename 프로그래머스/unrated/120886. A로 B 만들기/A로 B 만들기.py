def solution(before, after):
    answer = 0
    before = sorted(list(before))   # 리스트 뱐환 후 정렬
    after = sorted(list(after))     # 리스트 뱐환 후 정렬
    
    if before == after: # 두 리스트가 같을 경우
        answer = 1
    
    return answer