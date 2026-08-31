# https://school.programmers.co.kr/learn/courses/30/lessons/49994

from collections import defaultdict

def exists(MAP, d, A, B):
    if {A,B} in MAP[d]:
        return True
    return False

def solution(dirs):
    scale = 11  # 0~10 (원래 -5~+5)
    
    X = {i: [] for i in range(scale)}  # 세로이동 이력기록 (키: Y값, 값: )
    Y = {i: [] for i in range(scale)}   # 가로이동 이력기록
    
    NOW = (5, 5)
    count = 0
    
    for d in dirs:
        NEXT = (-10, -10)
        flag = 0  # 0:X(세로), 1:Y(가로)
        already = False
        
        match d:
            case 'U':
                flag = 0
                NEXT = (NOW[0], NOW[1]+1)
                already = exists(X, NOW[0], NOW[1], NEXT[1])
            case 'D':
                flag = 0
                NEXT = (NOW[0], NOW[1]-1)
                already = exists(X, NOW[0], NOW[1], NEXT[1])
            case 'L':
                flag = 1
                NEXT = (NOW[0]-1, NOW[1])
                already = exists(Y, NOW[1], NOW[0], NEXT[0])
            case 'R':
                flag = 1
                NEXT = (NOW[0]+1, NOW[1])
                already = exists(Y, NOW[1], NOW[0], NEXT[0])
            case _:
                print("문제 오류")
        
        # 유효 범위 체크 (0~10)
        if not (0 <= NEXT[0] <= scale-1 and 0 <= NEXT[1] <= scale-1):
            continue
        
        # 이동은 하되, 새로운 길이면 카운트
        if not already:
            count += 1
            if flag == 0:
                X[NOW[0]].append({NOW[1], NEXT[1]})
            else:
                Y[NOW[1]].append({NOW[0], NEXT[0]})
        
        NOW = NEXT
    
    return count

'''
## 문제조건
    - 좌표평면크기 내 캐릭터 상하좌우 이동 시 처음걸은 길 길이 계산
        > 좌표평면 벗어나면 무시(움직임X)
        > 왔던길 또 방문 시 무시(움직임O)
        
    * 좌표평면: -5~+5 -> 최대 10*11*2 = 220칸
        -> [핵심] 추적해야할게 좌표값이 아닌 좌표간 거리
            -> 선분을 추적할지, 출발-도착좌표를 추적할지
        
## 접근흐름
    [문제1]
    " 중복경로 지나려면, 시작-도착 점 모두 이미 방문한 길이어야함 "
    --> 그것만으론 조건충족안됨. 두 점 모두 방문한것만으론 선분방문여부 추적불가
    
    [문제2]
    " 그럼 선분은 어떻게 방문추적해야할까(좌표처럼 단순 2차배열에 값 넣기 불가) "
    --> 힌트: 선분을 만드는 두 점의 좌표 이용해서 만들기
    
    [해결] 
    1) 
    2) 좌표 이동시마다 시작좌표-이동좌표 중복확인 & 맵 내부인지 추적 후 이동
    
    (0,1) - (-1,1) -> 가로이동 : 가로 set맵에 Y 1: {0,-1} 기록
    (1,2) - (1,1) -> 세로이동 : 세로 set맵에 X 1: {2,1} 기록
    --> 현재좌표, 다음좌표 추적해서 바뀐게 가로면 가로set중에 전-후 추적
    
        ** ex: X 2:{1,0},{3,2} 
            -> x좌표 2인 부분 중 세로로 1<->0, 3<->2 이동 이력 나타냄
    
    
    
상하,좌우 따로
    UD: +1  +1    -1    +1
    LR:   -1  +1+1  -1-1
'''