def solution(n):
    answer = sum(list(map(int, str(n)))) # 각 자리수를 나누어 리스트에 저장 후 합계 연산
    return answer