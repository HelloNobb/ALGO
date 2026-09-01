# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 0
    
    D = {}
    # 각 의상종류-개수 키쌍으로 기록
    for c_set in clothes:
        if c_set[1] in D:
            D[c_set[1]] += 1
        else:
            D[c_set[1]] = 1
    # 수학적 조합 풀이 (모든 종류+1 해서 곱하기)
    tmp = 1
    for key in D:
        tmp *= (D[key]+1)
    answer = tmp-1
    
    return answer

'''
## input
[[의상이름1, 의상 종류],
[의상이름2, 의상종류], ...]

## output
조합개수

## 조건
- 의상종류 같으면 중복 불가
- 의상수 1~30개 -> 의상종류도 30개이하
- 의상이름은 중복없음

## 접근계획
- 모든 경우의수는, 의상종류 n에 따라
    (2^n - 1)개 (뽑고안뽑고 각자 2가지경우의수에따라)

> 뽑는 경우 -> (해당 종류의 의상개수)가지
> 안뽑는 경우 -> 1가지

====
1: dict에 종류-개수로 받기 (종류같으면 값+1
2: 각 키의 값 +1로다가 곱한다음 마지막에 -1해서 리턴

'''