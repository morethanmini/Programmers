n = int(input())
count = 0

for i in range(1, n+1):
    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        count += 1

print(count)

def solution(n):
    count = 0

    for i in range(1, n + 1):
        if i == 1:
            continue

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1

        return count