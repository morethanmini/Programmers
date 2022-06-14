absolutes = input().split()
signs = input().split()
answer = 0

for i in range(len(absolutes)):
    if signs[i]:
        answer += absolutes[i]
    else:
        answer -= absolutes[i]

print(answer)