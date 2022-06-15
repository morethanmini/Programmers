def solution(d, budget):
    d.sort()

    while budget < sum(d):
        d.pop()

    return len(d)

print(solution([1,3,2,5,4], 9))

"""
d를 정렬한 뒤 budget 보다 d의 sumd이 작아질 때 까지 d 에서 순차적으로 하나씩 꺼내준다.
지원해주는 부서의 크기는 남은 d의 원소 갯수로 구할 수 있다.
"""