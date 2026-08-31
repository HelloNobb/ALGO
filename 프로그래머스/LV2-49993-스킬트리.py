def solution(skill, skill_trees):
    answer = 0
    
    MAP = {}
    for i,s in enumerate(skill): #인덱스가 곧 진입차수개수
        MAP[s] = i
    
    
    for tree in skill_trees:
        count = 0 #각 트리당 발견된 트랙스킬 개수
        F = True
        for t in tree:
            if t in MAP: #트랙스킬 발견시,
                if count != MAP[t]:
                    F = False
                    break
                count += 1
        answer = answer+1 if F else answer
    
    return answer


'''
## 문제조건
[ 위상정렬: 순서스킬트리는 1개, 확인할 트리는 여러개 > 지킨 개수 return ]

## 접근흐름
[ 관건: 단순 존재여부가 아닌 순서 체크 >> 진입차수 체크하기 ]
    
CBD-> C: 0 B: 1 D: 2
    * 앞에서부터 스킬 발견 시 count만큼의 진입차수 가졌는지 체크, count++처리
    * 끝까지 문제없으면 ok

'''