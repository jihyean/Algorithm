def solution(babbling):
    answer = 0
    spells = ["aya", "ye", "woo", "ma"]
    
    for babble in babbling:
        for spell in spells:
            babble = babble.replace(spell, ' ', 1) # 할 수 있는 발음 공백으로 치환
        
        babble = babble.replace(' ', '')    # 공백 삭제
        
        if(babble == ""):                   # 발음할 수 있는 조합일시 개수 1증가
            answer = answer + 1
    
    return answer