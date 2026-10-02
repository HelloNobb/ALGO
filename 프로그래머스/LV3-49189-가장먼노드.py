# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    
    MAP = [[] for _ in range(n+1)]
    for one, two in edge:
        MAP[one].append(two)
        MAP[two].append(one)
    
    FAR = [500001] * (n+1)
    FAR[1] = 0
    
    Q = deque()
    Q.append(1)
    while Q:
        now = Q.popleft()
        
        for next in MAP[now]:
            if FAR[next] <= FAR[now]+1:
                continue
            
            FAR[next] = FAR[now]+1
            Q.append(next)
    
    max_idx = 1
    cnt = 0
    for i in range(1, n+1):
        if FAR[max_idx] < FAR[i]:
            cnt = 1
            max_idx = i
        elif FAR[max_idx] == FAR[i]:
            cnt += 1
            
    
    
    return cnt


'''
## 조건
    - 1부터의 최단경로 구했을때 가장 먼 노드 개수
    
    * 노드수: 2만
    * 간선수: 5만


## 접근
    [ 가중치 1인 다익스트라 (1-> 각 노드 최단경로)]
    0: 그래프 생성, 간선개수 초기화
        1: 2,3
        2: 1,3,4
        3: 1,2,4,6
        ...
        
        far = [-1,-1,...]
        far[1] = 0
        
    1: BFS로 구하면 됨 순차적으로 자식들 (간선가중치 모두 동일)



## 회고 =====
> 얘는 말그대로 순서대로 한번 처리하면 그게 최단거리 확정이라, visited 추적했으면 더 좋았다

'''