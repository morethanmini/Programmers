def solution(n):
    arr = ''

    for i in range(n):
        if i % 2 == 0:
            arr += '수'

        else:
            arr += '박'

    return arr