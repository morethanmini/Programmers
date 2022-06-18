def solution(n):
    answer = []

    for i in range(len(n)):
        for j in range(i+1, len(n)):
            answer.append(n[i] + n[j])

    return sorted(list(set(answer)))

print(solution([2, 1, 3, 4, 1]))