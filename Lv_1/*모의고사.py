def solution(answers):
    answer = []

    a1_arr = [1, 2, 3, 4, 5]
    a2_arr = [2, 1, 2, 3, 2, 4, 2, 5]
    a3_arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a1_arr[i % 5]:
            cnt[0] += 1

        if answers[i] == a2_arr[i % 8]:
            cnt[1] += 1

        if answers[i] == a3_arr[i % 10]:
            cnt[2] += 1

    max_cnt = max(cnt)

    for i in range(3):
        if max_cnt == cnt[i]:
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))