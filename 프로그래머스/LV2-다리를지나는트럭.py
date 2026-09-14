# https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    
    while bridge_weight > 0 or trucks:
        
        done = bridge.popleft()
        bridge_weight -= done
        
        # -- trucks 비었으면 인덱스 에러 남. 놓치지 않기 --
        if trucks and bridge_weight + trucks[0] <= weight:
            new_ = trucks.popleft()
            bridge.append(new_)
            bridge_weight += new_
        else:
            bridge.append(0)
        
        time += 1
        
    return time

'''
## 문제조건
[ 길이제한,무게제한있는 1줄다리에 
  제각각 무게인 트럭들을 모두 순서대로 건너게 할 때 걸리는 최소시간 ]
 
    * 다리길이: 1 ~ 1만
    * 무게제한: 1 ~ 1만
    
    * 트럭무게: 1 ~ 무게제한
    * 트럭개수: 1 ~ 1만

## 접근흐름
	[계획 1] 한번에 올라갈 수 있는 트럭 뭉텅이로 넣기 반복
    - 한번에 올라갈 수 있는 트럭 순서대로 한번에 뽑아 건넘처리 (= 1사이클)
        > time += (다리길이 + 이번에 올라간 트럭무게합)

	== [반례] 뭉텅이로 판단 불가. 앞 트럭이 빠지는 타이밍 따라 다른 트럭 중간에 넣을 수 있음
 
	== [힌트] 1초 단위 시뮬레이션 방식 (--> 생각은 했으나 더 간단한 방법같아서 계획 1로 함..)
 
	
	[계획 2] 1초 단위 시뮬방식으로, 시간 1씩 추가하며 매번 큐에 넣고 남은 길 -1 처리.
		0: 다리길이의 큐 생성 후 0으로 초기화
		1: 맨앞 큐값 pop -> 남은 무게 업데이트 (남은무게 -= 방금꺼낸무게값)
		2: 이번차례 트럭 무게값이 남은 무게 이하이면, 트럭값 큐에 넣기 / 불충족시 큐에 0 넣기(=안넣음)
		3: 시간 += 1 & 남은무게 업데이트 (남은무게 += 방금넣은무게값)
		--> 더 넣을 트럭 없음 && 다리큐 무게값 0 일때까지 반복. 
		4: 시간값 return
    어차피 다리길이가 
'''