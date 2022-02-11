c = int(input())

for _ in range(c):
    nums = list(map(int,input().split()))
    avg = sum(nums[1:])/nums[0]
    over_s = 0
    for num in nums[1:]:
        if num > avg:
            over_s += 1
    rate = (over_s / nums[0]) * 100

    print(f'{rate:.3f}%')