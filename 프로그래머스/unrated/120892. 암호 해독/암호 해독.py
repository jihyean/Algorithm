def solution(cipher, code):
    answer = ''
    cipher_list = list(cipher)
    
    for i in range(code, len(cipher)+1, code):  # code 만큼 증가
        answer = answer + cipher_list[i-1]      # 인덱스는 0부터 시작하므로 -1

    return answer