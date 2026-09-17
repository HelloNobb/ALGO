'''
h 이상인 값이 h 이상개 있는가?
-> 내림차순 정렬 후
-> index + 1 >= value 를 만족할 때의 value

=> 이해를 잘못했다. h가 꼭 배열 내에 있는 값일 필요는 없음
# 9 7 6 2 1
-> 2가 되는게 아니라 3임 (3번이상 인용된게 3개 이상)
-> value가 아니라 index 기준으로 계산해야 할듯

# 회고
지문을 자세히 이해하지 않았고, 반례를 차분하게 생각하지 않아서 왜 틀린지 이해하지 못하다 시간이 많이쓰임ㅜ
'''

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1      # 논문의 수
        else:
            break
            
    return answer
