# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq

def solution(N, road, K):
    answer = 0

    # 딕셔너리 초기화
    MAP = [[] for _ in range(N+1)]
    for r in road:
        one = r[0]
        two = r[1]
        di = r[2]
        
        MAP[one].append((di, two))
        MAP[two].append((di, one))
        
    dist = [500000] * (N+1)
    dist[1] = 0
    
    heap = [(0,1)] #(최단거리,정점)  --순서: 거리기준 정렬위해
    while heap:
        di, NOW = heapq.heappop(heap)
        # 이미 더 짧은 경로로 처리된 애면 스킵
        if di > dist[NOW]:
            continue
        
        # 연결된 애들 최단거리배열 업데이트 -> 업데이트된애들은 힙에 넣기 (또 줄줄이 업데이트해야하므로)
        for d, NEXT in MAP[NOW]:
           next_di = d + di
           # 이웃 업데이트했을때 더 짧은 거리면 이웃을 갱신 + 힙에 넣기
           if next_di < dist[NEXT]:
                dist[NEXT] = next_di
                heapq.heappush(heap, (next_di, NEXT))
    
    return sum(1 for i in range(1, N+1) if dist[i] <= K)





    # while Q:
    #     FROM = Q.popleft()
        
    #     for info in MAP[FROM]:
    #         TO = info[0]
    #         di = info[1]
    #         # 거리업데이트 후 넣기
    #         dist[TO] = min(dist[TO], dist[FROM] + di)
    #         if not visited[TO]:
    #             visited[TO] = True
    #             Q.append(TO)

    # for i in range(1, N+1):
    #     if dist[i] <= K:
    #         answer += 1

    # return answer


'''
## 조건
	- 1번에서 출발 , 배달시간 K이하인곳 구하기

	* 마을(N) : 1~50
	* 길 개수 : 1~2000
 
	/ 두 점 잇는 도로가 2개 이상일 수 있음
	/ 동떨어진 애 없음

## 접근
	[dijkstra]: 특정 정점으로부터 각 정점으로의 최단거리 구하기 (거리가중치 >= 0)
	
	0: 거리 그래프 만든다. (이때, 두 정점사이 도로가 2개 이상이면 최단으로 업데이트)
		MAP = {
			1: (2,1), (4,2)
			2: (1,1), (3,3), (5,2)
			3: (2,3), (5,1)
			4: .... 
  		}
  
		dist = [50만] x N , dist[1] = 0
  
	1: 기준점인 1번부터, 이웃 꺼내 큐에 넣고 (2,4) 거리 업데이트 (dist[2] = 1, dist[4] = 2)
	2: 기준 2 걔네 연결된애들도 다 큐에 넣고 거리 업데이트 
 
	== [EDGE] BFS식으로 하면 안됨. dist중에 최단거리인애 먼저 찾아서 greedy하게 해야함.
	- 매번 dist가 최소인걸로 안하고 시작점으로부터 이어진 애부터 고르면,
		만약 다른 애 통해서 다시 돌아와 1번과 이어진애로 오는게 더 최단일 경우 ,
		값은 업데이트 되나 걔와 연결된 다른 애들은 최단으로 업데이트 안되는 예외 발생
  
	>> 자료구조를 heap을 써서 매번 최소거리인애 뽑아써야함
'''
