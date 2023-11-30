def solution(num_list):
    
    if(num_list[-1] > num_list[-2]):                    # 마지막 원소가 클 경우
        num_list.append(num_list[-1] - num_list[-2])    # 배열 리스트에 (마지막 원소 - 그 앞 원소) 값 추가
    else:                                               # 마지막 원소가 크지 않을 경우
        num_list.append(num_list[-1] * 2)               # 배열 리스트에 (마지막 원소 * 2) 값 추가
        
    return num_list