def solution(bin1, bin2):
    bin3 = int(bin1, 2) + int(bin2, 2)  # 10진수로 변환 후 더하기 연산
    answer = str(bin(bin3)[2:])         # 10진수를 다시 2진수로 변환
    return answer