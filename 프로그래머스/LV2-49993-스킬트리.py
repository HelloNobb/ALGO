'''
# solution
스킬트리에서 스킬과 겹치는 부분만 남기고
남긴부분과 skill이 같은지 검사
'''
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        filtered = ""
        for char in skill_tree:
            if char in skill:
                filtered += char
        if filtered == skill[:len(filtered)]:
            answer += 1
            
    return answer