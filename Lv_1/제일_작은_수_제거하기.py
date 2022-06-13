arr = [10]

if len(arr) == 1:
    arr.append(-1)

else:
    arr.remove(min(arr))

print(arr)