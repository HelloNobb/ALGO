'''
최소값으로 목적지 찾아가기

# BFS

- 맵 밖, 벽으로는 이동 불가
- 상대 진영에 도착하는 경우의 수 없으면 -1 return
- 최단거리로 갈수 있는 방법 return

# solution
큐에 '이동 가능한 좌표' 저장
-> 이때 visited 처리
하나씩 꺼내면서 해당 위치에서 '이동 가능한 좌표' 큐에 추가
-> visited인 좌표, 벽, 맵 밖은 불가
-> 큐에 추가되는건 x, y, '몇번 이동한 칸인지'

visited : [x][y]

# pseudo code
1. maps 반복하며 맵데이터 받아옴
2. 현재위치(0,0) 큐에 넣음
3. 큐가 빌때까지 큐에 있는걸 꺼내 상하좌우 이동 체크
    - 이동할 수 있으면 이동칸 + 1 해서 큐에 넣음
4. 이동한 좌표가 목적지일 경우 break 하고 이동칸 + 1해서 return
    - 큐가 빌 경우 -1 return

'''
from collections import deque

def solution(maps):
    answer = 0    
    # 2. 현재위치, 움직인횟수(0,0,0) 큐에 넣음
    que = deque()
    que.append([0,0,1])
    # 3. 큐가 빌때까지 큐에 있는걸 꺼내 상하좌우 이동 체크
    #     - 이동할 수 있으면 이동칸 + 1 해서 큐에 넣음
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[True for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = False
    
    while que:
        temp = que.popleft()
        
        for i in range(4):
            tempX = temp[0] + dx[i]
            tempY = temp[1] + dy[i]
                
            # 갈수 있는지 체크
            if(tempX >= 0 and tempX < len(maps) and tempY >= 0 and tempY < len(maps[0])):
                # visited 체크
                if(not visited[tempX][tempY]):
                    continue
                # 벽인지 체크
                if(maps[tempX][tempY] != 0):
                    # 4. 이동한 좌표가 목적지일 경우 break 하고 이동칸 + 1해서 return
                    if(tempX == len(maps) - 1 and tempY == len(maps[0]) - 1):
                        return temp[2] + 1
                        
                    else:
                        que.append([tempX, tempY, temp[2]+1])
                        visited[tempX][tempY] = False
    if(answer == 0):
        answer = -1
    
    return answer
