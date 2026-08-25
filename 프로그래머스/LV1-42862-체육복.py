# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0
    
    ALL = [1]*n
    for i in lost:
        
        ALL[i-1] -= 1
    for i in reserve:
        ALL[i-1] += 1
    
    count = 0
    for i in range(n):
        if ALL[i] == 0:
            # 구조 요청 (왼,오)
            if i != 0 and ALL[i-1] > 1:
                ALL[i-1] -= 1
                ALL[i] += 1
            elif i < n-1 and ALL[i+1] > 1:
                ALL[i+1] -= 1
                ALL[i] += 1
            # 구조 실패시
            else:
                count += 1
    answer = n-count
    return answer

'''

## 접근 흐름
    1: 걍 30짜리 배열에 모두 1넣어놓고,
        lost돌려서 -1씩, reserve돌려서 +1씩
    2: 배열 돌면서 값0인거 있으면,앞뒤확인해서 2인애 있음 주고 넘기기
        > 없으면 count+1하고 넘기기
    
'''