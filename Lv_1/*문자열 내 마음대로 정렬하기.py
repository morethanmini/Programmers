def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n],x))

print(solution(["sun", "bed", "car"], 1))

"""
1. sort, sorted에 key인자를 넣어줌으로써 정렬 기준을 정할 수 있다.
2. key 기준으로 정렬을 할 경우 오직 key 기준으로만 정렬을 한다. key이외의 나머지 요소에 대해선 정렬되지 않음.
3. lambda를 이용한 key 설정에서 튜플을 넣어줌으로써 정렬의 우선순위를 지정할 수 있다.
"""