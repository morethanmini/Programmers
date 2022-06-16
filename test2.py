def check(a, b, c):
    total = a + b + c
    for i in range(2, total):
        if total % i == 0 :
            return False
    return True

print(check(1,2,4))