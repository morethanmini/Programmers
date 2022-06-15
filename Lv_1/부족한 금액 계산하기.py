price, money, count, = map(int, input().split())
sum = 0

for i in range(1, count+1):
    q = i * price
    sum += q

lack_money = sum - money

if lack_money < 0:
    print(0)

print(lack_money)


def solution(price, money, count):
    sum = 0

    for i in range(1, count + 1):
        q = i * price
        sum += q

    lack_money = sum - money

    if lack_money < 0:
        return 0

    return lack_money