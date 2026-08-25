'''
# 조건
- 각 알파벳 처음은 A

# return
조이스틱 조작 횟수의 최솟값
    - 커서 옮기는 횟수(len - 1)
    - 알파벳 옮기는 횟수 (0 ~ 13)
        -> 26가지 알파벳중 '뒤로' or '앞으로' 가는것중 유리한 방법으로 이동
        -> 1~14 앞으로 / 15~26(90) 뒤로
        -> 알파벳이 주어지면 몇번 이동해야 하는지 바로 나옴
        -> A 가 65. 78까지 앞으로.
        
        ! JAZ 의 경우, 가운데가 A면 바로 왼쪽으로 한번 이동 가능
            -> 다음으로 이동 시
                - 출발 index
                를 저장하고,이후 A가아닌 다른 문자를 만날 경우
                -> 출발 index와 현재 index를 비교, '뒤로 갔는게 빨랐는지', '그대로 오는게 빨랐는지' 검사.
                    -> 뒤로가는게 빨랐을 경우 answer -= 1
            -> A를 만났을 때, '쭉 가서 A가 아닌걸 만나는 수'와 '일단 뒤로가서 A가아닌걸 만나는 수' 검사
        [1] 2 [3] 4 5 6 7 8 9 [10]

# 회고
! 풀이 찾아본 문제
스터디 시작하고 풀었던 문제중 가장 어려웠다. 좌우이동의 최소값 구하는 방식을 정확히 떠올리지 못했다.
시작할때 문제조건 제대로 안보고 좌우이동 생각안하고 그냥 len - 1 때려박았다가 시간낭비 많이했다.

-> 문제 잘 읽어 요구조건 정확히 분석하기

'''

def solution(name):
    answer = 0
    
    # 상, 하 이동 최소값
    for char in name:
        char_num = ord(char)
        if char_num > 78:      # 뒤로 이동하는 케이스
            answer += 90 - char_num + 1
        else:
            answer += char_num - 65
    
    # 좌, 우 이동 최소값
    n = len(name)
    min_move = n - 1
    
    for i in range(n):
        next_idx = i + 1
        
        # 현재위치(i) 에서 다음 A가아닌 문자가 나오는 위치(next_idx)를 구함
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        # 구간을 3개로 나눈다.
        # 시작~현재(front_area) / 현재~다음문자(연속된 A가 있는 구간) / 다음문자~끝(back_area)
        front_area = i
        back_area = n - next_idx
        
        # 시작~현재를 먼저 하고 뒤로가는 case
        front_first = (front_area * 2) + back_area
            
        # 뒤 먼저 갔다가 현재로 돌아오는 case
        back_first = (back_area * 2) + front_area
        
        min_move = min(min_move, front_first, back_first)
    
    answer += min_move
    return answer