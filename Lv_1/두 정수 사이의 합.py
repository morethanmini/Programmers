a, b = map(int, input().split())
sum = 0

for i in range(a, b+1):
    sum += i

print(sum)

def solution(a, b):
    sum = 0
    c, d = min(a, b), max(a, b)
    for i in range(c, d+1):
        sum += i

    return sum