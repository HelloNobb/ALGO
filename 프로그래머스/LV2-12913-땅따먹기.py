# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0

    for i in range(1, len(land)):
        # ----
        #for j in range(4):
            # land[i][j] = land[i][j] + max(land[i-1][k] for k in range(0,4) if k != j) 
		# ----> 코드는 간결하나 제너레이터+max가 오버헤드 발생시킴
        before = land[i-1]
        land[i][0] += max(before[1], before[2], before[3])
        land[i][1] += max(before[0], before[2], before[3])
        land[i][2] += max(before[0], before[1], before[3])
        land[i][3] += max(before[0], before[1], before[2])
        
    # answer = max(land[len(land)-1][k] for k in range(0,4)) -->아래처럼 간결하게
    answer = max(land[-1])

    return answer


''' 
## 문제조건
[ 각 행마다 하나씩 선택하여 최고점 만들기 ]
    - 다음 행에선 전 행 인덱스값 제외하고 선택가능 **
    - 최대 열 4개, 행 10만개
    
## 접근흐름
    [문제] 모든 경우의수는 못 구함.(4*3^(10만-1))
    
    [계획] "어차피 큰값 2개중 하나 선택하는 문제"
    - 두가지경우 찾기 (첫열이 max , 첫열이 두번째max)
    
    ==> [반례]
    row0: [10,  9,  1,  1]
    row1: [ 1,  2,  3,  4]
    row2: [ 1,  1,  1, 10]
    
    ==> [힌트] DP로 접근
    
    [계획2]
    - DP로 i행에서 1~4열 각각 선택했을때의 최대값 기록
        = i-1행의 1~4열 각각 선택했을때의 최대값 기록해둔거 참고해서,
            그 중 i행에서 선택하려는 열 외의 최대DP값인 열로 선택
    
    
'''