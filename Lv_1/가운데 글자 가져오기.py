s = input()

q = len(s)
t = q // 2

if q % 2 == 1:
    print(s[t])

else:
    print(s[t-1]+s[t])

def solution(s):
    q = len(s)
    t = q // 2

    if q % 2 == 1:
        return s[t]

    else:
        return s[t - 1] + s[t]