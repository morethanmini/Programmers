n = input().lower()
p = n.count('p')
y = n.count('y')

if p == 0 and y ==0:
    print('True')

if p == y:
    print('True')
elif p != y:
    print('False')

def solution(n):
    n = n.lower()
    p = n.count('p')
    y = n.count('y')

    if p == 0 and y == 0:
        return True

    if p == y:
        return True
    elif p != y:
        return False