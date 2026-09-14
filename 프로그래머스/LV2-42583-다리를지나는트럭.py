'''
다리를 큐로 구현. 
다리의 무게 : 큐 전체 값들의 합

# solution
반드시 순서를 지키면서 다리에 올라가야 하므로, 실제 큐에 넣었다가 뺴면서 시뮬레이션.
트럭의 길이는 0으로 채워 구현

'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge = deque([0] * bridge_length)
    current_weight = 0  
    time = 0
    truck_idx = 0       

    while truck_idx < len(truck_weights) or current_weight > 0:
        time += 1

        removed = bridge.popleft()
        current_weight -= removed

        if truck_idx < len(truck_weights):
            next_truck = truck_weights[truck_idx]
            if current_weight + next_truck <= weight:
                bridge.append(next_truck)
                current_weight += next_truck
                truck_idx += 1
            else:
                bridge.append(0)  
        else:
            bridge.append(0)      

    return time
