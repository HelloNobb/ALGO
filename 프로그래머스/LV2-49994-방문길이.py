'''
x,y로 visited 관리할게 아니라 선으로{[출발좌표], [도착좌표]} 관리?
-> 좌표의 방향은 상관없으므로 set
-> x,y좌표의 위치는 상관있으므로 list

맵 밖으로 안나가게 현재좌표 체크

# solution
for order in 명령어:
    beforeCoord = coord
    
    if(order == 'U'):
        if coord[1] >= 5:
            continue
        else:
            coord[1] += 1
    elif order == 'D':
        if coord[1] <= -5:
            continue
        else:
            coord[1] -= 1
    elif order == 'R':
        if coord[0] >= 5:
            continue
        else:
            coord[0] += 1
    elif order == 'L':
        if coord[0] <= -5:
            continue
        else:
            coord[0] -= 1
    
    visited.add({beforeCoord,coord})
        
        
# 회고
문제를 풀어도 코드가좀 더럽다. 시간될때 리팩토링 해봐야 할듯하다.
set 자료형에 대해 더 잘 알아가는 시간이었다
=> list는 set에 못들어간다. 
---
파이썬에서 set과 dict의 key는 빠른 탐색을 위해 해시값을 사용합니다.
하지만 list는 언제든 값이 바뀔 수 있는 가변 객체이므로 해시값을 생성할 수 없어 set의 원소로 넣을 수 없습니다.
---

'''
def solution(dirs):
    answer = 0
    coord = [0,0]
    visited = set()
    
    for order in dirs:
        beforeCoord = tuple(coord)

        if(order == 'U'):
            if coord[1] >= 5:
                continue
            else:
                coord[1] += 1
        elif order == 'D':
            if coord[1] <= -5:
                continue
            else:
                coord[1] -= 1
        elif order == 'R':
            if coord[0] >= 5:
                continue
            else:
                coord[0] += 1
        elif order == 'L':
            if coord[0] <= -5:
                continue
            else:
                coord[0] -= 1
        nowCoord = tuple(coord)
                
        visited.add((beforeCoord,nowCoord))
        visited.add((nowCoord,beforeCoord))
        
        
    answer = len(visited) // 2
    
    return answer