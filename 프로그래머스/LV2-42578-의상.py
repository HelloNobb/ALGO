'''
(가짓수+선택x)로 곱한뒤 - (아무것도 선택하지 않는 경우)

# solution
dict로 카태고리별로 분류
-> dict[key] = value
    키 있으면 append / 없으면 리스트 만들어 추가
각 key의 value수 + 1만큼 곱하고 - 1 리턴
-> for key in dict:
        len(dict.get(key)) + 1
'''

def solution(clothes):
    answer = 1
    dict = {}
    
    for clothe in clothes:
        if clothe[1] in dict:
            dict[clothe[1]].append(clothe[0])  
        else:
            dict[clothe[1]] = [clothe[0]]
    
    for key in dict:
        answer *= len(dict.get(key)) + 1
    
    return answer - 1