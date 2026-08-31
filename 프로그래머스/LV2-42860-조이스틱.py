# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    # 상하 이동: 각 글자마다 A에서의 최소 거리
    updown = 0
    for ch in name:
        d = ord(ch) - ord('A')
        updown += min(d, 26 - d)
    
    # 좌우 이동: 모든 A구간에 대해 꺾는 경우 비교
    n = len(name)
    leftright = n - 1  # 기본값: 오른쪽 직진 (짧은 길 있음 갱신 예정)
    
    for i in range(n): # i: 꺾는 지점
        # i 다음부터 연속 A구간 끝 찾기
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        right = i
        left = n - next_i
        
        leftright = min(leftright, right * 2 + left)   # 오른쪽 먼저
        leftright = min(leftright, right + left * 2)    # 왼쪽 먼저
    
    return updown + leftright

# #알파벳간 거리 계산
# def get_distance(FROM, TO): 
#     d1 = abs(ord(TO)-ord(FROM))
#     d2 = 26 - d1
    
#     return min(d1, d2)

# #정방/역방 중 가장 가까운 타깃까지거리
# def get_distance2(start, ARR): 
#     for i in range(len(ARR))
            
    

# def solution(name):
#     # [ A 위치: 1, 나머지: 0 ] 배열 생성
#     DONE = [0]*len(name)
#     for i, n in enumerate(name):
#         if n == 'A':
#             DONE[i] = 1
    
#     # 이동횟수 계산
#     count = 0
#     idx = 0
#     while sum(DONE) != len(name):
#         # 1: 현재 위치 처리 (알파벳이동계산)
#         count += get_distance('A', name[idx])
#         DONE[idx] = 1
        
#         # 2: 다음 타깃 최단거리 계산 (정/역방)
        
    
#     return count

'''
## 문제조건
    - 모든 자리가 A로 시작
    - 상하: 알파벳 변경 (맨앞-맨뒤 이동 가능)
    - 좌우: 바꿀위치 변경 (맨앞-맨뒤 이동 가능)

## 접근흐름
    0: 알파벳 간 간격 (시작-목적지) 정방/역방 중 짧은 거리 반환 함수
    1: 순서대로 A가 아닌 알파벳 목적지로 이동(이것도 최단거리로 제일 먼저 나오는 알파벳까지)
    
    0: util 함수들 구현
        * 알파벳간 최단 간격 얻는 함수 (정방/역방)
        * 다음 타깃 위치 찾기 (현재위치->다음위치 최단인 애로)
    1: 문자길이만큼 A아니면 0, A면 -1 넣은 배열 생성
        -> 

======= 정답 코드 확인 후...
    ** 핵심: 최악이래봤자 2회만 꺾어지는 경우임.
        [결국 경우의수 3가지]
        -> 1) 걍 오른쪽 직진
        -> 2) 오른쪽먼저 -> 돌아와서 왼쪽
        -> 3) 왼쪽먼저 -> 돌아와서 오른쪽

'''