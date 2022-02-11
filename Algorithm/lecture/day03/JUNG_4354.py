# 927: 리스트3 - 자가진단7

success = 0

for i in range(5):
    nums = list(map(int,input().split()))
    avg = sum(nums)/len(nums)
    if avg >= 80:
        success += 1
        print('pass')
    else:
        print('fail')

print(f'Successful : {success}')

# nums = [list(map(int,input().split())) for _ in range(5)]
# counting = 0

# for i in range(5):
#     avg = sum(nums[i])/4
#     if avg >= 80:
#         counting += 1
#         print('pass')
#     else:
#         print('fail')
# print(f'Successful : {counting}')

# for i in range(5):
#     total = 0
#     for j in range(4):
#         total += score[i][j]
#     avg = total/4
#     if avg >= 80:
#         counting += 1
#         print('pass')
#     else:
#         print('fail')
# print(f'Successful : {counting}')