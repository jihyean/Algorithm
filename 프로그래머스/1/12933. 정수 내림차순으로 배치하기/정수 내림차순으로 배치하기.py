def solution(n):
    str_list = list(str(n))
    str_list.sort(reverse=True)
    answer = int(''.join(str_list))
    return answer