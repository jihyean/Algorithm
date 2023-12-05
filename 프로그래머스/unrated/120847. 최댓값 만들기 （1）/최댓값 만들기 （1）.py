def solution(numbers):
    numbers.sort(reverse = True)    # 역순 정렬
    answer = numbers[0] * numbers[1]# 가장 큰 값과 두 번째로 큰 값 곱하기
    return answer