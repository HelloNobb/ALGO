'''
- 여분을 가지고 있는 사람이, 자신/바로한칸옆 사람에게 빌려줄 수 있음

# solution
- reserve가 우선순위를 두고 체육복을 빌려주면 '다른사람이 빌려줄 수 있는데 내가 빌려줘서 못받는사람 발생' 케이스 방지가능
-> reserve가 오름차순 정렬되어있다는 가정 하에
1. 자기자신
2. 자기 앞번호
3. 자기 뒷번호

list에서 제거하는건 시간복잡도가 높기 때문에
set으로 변경

# psuedo code
set 자료형으로 변환    set(list)
answer = n - len(lost)

자기꺼 먼저 빌린애 제거

for num in set:
    lost에서 순서대로 검사
    빠질때 마다 answer++

'''

def solution(n, lost, reserve):
    answer = 0

    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    real_reserve = sorted(real_reserve)

    for num in real_reserve:
        if num - 1 in real_lost:
            real_lost.remove(num - 1)
        elif num + 1 in real_lost:
            real_lost.remove(num + 1)
    answer = n - len(real_lost)
    return answer
