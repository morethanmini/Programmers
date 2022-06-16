from itertools import combinations

def check(a, b, c):
    total = a + b + c
    for i in range(2, total):
        if total % i == 0 :
            return False
    return True

data = [1, 2, 3, 4]
result = list(combinations(data, 3))
answer = 0

for i in result:
    if check(i[0], i[1], i[2]):
        answer += 1

print(answer)