def solution(n):
    count = 0

    for i in range(2, n):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
            else:
                count += 1

    return count
#print(solution(7))
# def solution():

n = int(input())

answer = set(range(2, n+1))

for i in range(2, n+1):
    if i in answer:
        answer -= set(range(i*2, n+1, i))
print(answer)