# ALGO
[ 코딩테스트 준비를 위한 알고리즘 문제 풀이 기록 저장소 ]

풀고 끝내는 게 아니라, 나중에 다시 봤을 때 핵심을 30초 안에 떠올릴 수 있도록 정리한다.

## 브랜치 규칙

- `main`: 규칙(README) + 문제 목록(PROBLEMS.md)
- `free/{닉네임}`: 자유롭게 push하는 작업 공간
- `review/{닉네임}`: 리뷰 완료된 코드만 머지. `free/{닉네임}` → `review/{닉네임}`으로 PR, 나머지 멤버 중 1명 이상 승인 필수

## 파일 구조

```
leetcode/
  Easy-70-ClimbingStairs.py
  Easy-REVIEW.md
  Medium-198-HouseRobber.py
  Medium-REVIEW.md
프로그래머스/          # W1~W6 (이전 기록)
  LV2-43165-타겟넘버.py
  LV2-REVIEW.md
```

### leetcode (W7~)
- 소스코드: `{난이도}-{문제번호}-{문제이름}.py`
  - 난이도: `Easy` / `Medium` / `Hard`
  - 문제이름: 영어 제목을 띄어쓰기 없이 단어 첫 글자만 대문자로 (예: `Unique Paths II` → `UniquePathsII`)
- 리뷰: `{난이도}-REVIEW.md` (난이도별 1개)

### 프로그래머스 (W1~W6)
- 소스코드: `LV{레벨}-{문제번호}-{문제이름}.py`
- 리뷰: `LV{레벨}-REVIEW.md` (레벨별 1개)

## REVIEW 작성 양식

### {플랫폼} - {문제번호}. 문제이름 / [링크](URL)
(예: `### LeetCode - 198. House Robber / [링크](https://leetcode.com/problems/house-robber/)`)
- **유형**: DFS / DP / 그리디 / 등등
- **핵심**: (1~2줄)
- **삽질**: (1~2줄)
- **시간복잡도**: O(N)
---
