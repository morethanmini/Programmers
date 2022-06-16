def solution(nums):
    answer = len(nums) / 2

    nums = set(nums)

    if answer > len(nums):
        answer = len(nums)

    return answer

print(solution([3,3,3,2,2,2]))