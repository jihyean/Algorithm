def solution(cards1, cards2, goal):
    
    # goal(원하는 카드 배열)을 다 만들때까지
    while len(goal) != 0:
        if len(cards1) > 0 and goal[0] == cards1[0]:    # 첫단어가 첫번째 카드뭉치의 첫 카드와 같을때
            cards1.pop(0)                               # 해당 카드 삭제
            goal.pop(0)                                 # 해당 단어 삭제(넘김)

        elif len(cards2) > 0 and goal[0] == cards2[0]:  # 첫단어가 두번째 카드뭉치의 첫 카드와 같을때
            cards2.pop(0)
            goal.pop(0)

        else:               # 단어 배열 만들기 실패
            answer = 'No'
            return answer   # 'No' 반환
        
    answer = 'Yes'          # 단어 배열 만들기 성공
    return answer           # 'Yes' 반환