from collections import deque

def dfs(MAP, Q):
    
    while Q:
        N = len(MAP[0])# 가로 = [][*]
        M = len(MAP)# 세로 = [*][]
        
        x, y = Q.popleft() # 현위치
        
        # 만약 목적지에 도착했다면, 그 값 리턴하기
        if x == M-1 and y == N-1:
            return MAP[x][y]

        # 상하좌우 확인하여 1이면 값 업데이트하고 큐에 넣기
        goX = [1,-1,0,0]
        goY = [0,0,1,-1]
        for i in range(4):
            nextX = x+goX[i]
            nextY = y+goY[i]
            
            if (nextX < 0 or nextX >= M or nextY < 0 or nextY >= N):
                continue
			# 다음 곳이 아직 방문 안한 곳이면, 값 업데이트(현위치값+1)하고 큐에 넣기
            if MAP[nextX][nextY] == 1:
                MAP[nextX][nextY] = MAP[x][y]+1
                Q.append((nextX, nextY))
    # 큐 비었는데 리턴 안됐단 건 도달 못했단 얘기
    return -1
            

def solution(maps):
    answer = 0
    
    q = deque()
    q.append((0,0))
    answer = dfs(maps, q)
    
    return answer


'''
## 문제 조건
	[ nxm 게임판에서 (0,0)에서 (n-1,m-1)로 가는 최단거리 구하기 ]
    - (1,1) -> (n,m) 도달 목표
    - 가장 빠르게 가는 경로 길이 출력 (도달 못하는 경우 -1)

## 접근 계획
[ BFS: 최단경로 찾기 ]
 - 시작점 큐에 넣고, 큐 빌때까지 하나씩 뽑아 상하좌우 탐색 후 조건에 맞으면 그자리값 업데이트하고 큐에 넣고 반복
 - 다음 위치값이 1이면(=방문X), 현재위치값+1로 값 업데이트한다. (=방문여부 표시이자, 현재 이동거리 표시)
 - 만약 1이 아닌 경우(0: 막힌자리 / 2이상: 이미 방문한적있는자리 = 갈필요없음. 최단거리아닐테니) 무시한다.
 
## 핵심
 - 이차배열 [][]에선, 행이 앞자리([*][]) / 열이 뒷자리([][*])
	-> len(MAP): 행길이, len(MAP[0]): 열길이
 
 - BFS 최단경로 : 큐에 넣기 전에 미리 방문처리하고 넣고, 목적지 도달할때까지 하나씩 뽑고 다시 탐색 반복
'''