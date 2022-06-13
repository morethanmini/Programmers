n = [2,1,3,4,1]
answer = []

for i in range(len(n)):
    for j in range(i+1, len(n)):
        answer.append(n[i] + n[j])

print(sorted(list(set(answer))))