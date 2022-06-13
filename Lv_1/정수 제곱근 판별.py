n = int(input())
num = n ** 0.5

if num == int(num):
    answer = (num + 1) ** 2
else:
    answer = -1

print(answer)