'''
http://school.programmers.co.kr/learn/courses/30/lessons/43165

## IO 예시
[1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

>> I: [1,1,1,1,1] , 3
>> O: 5


## 접근방법
- dfs로 각 숫자가 +인 경우, -인경우 돌려서 전체 돌았을때, target값인 경우 answer+=1
'''

def dfs(N, t, now, idx):
    if idx == len(N):
        return 1 if now == t else 0
    return dfs(N, t, now + N[idx], idx+1) + dfs(N, t, now - N[idx], idx+1)

def solution(numbers, target):
    answer = dfs(numbers, target, 0, 0)
    return answer