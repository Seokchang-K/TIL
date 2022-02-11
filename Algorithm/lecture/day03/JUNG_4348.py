# 921:리스트 3 - 자가진단1

n = int(input())
# nums = []
# for i in range(n):
#     nums.append((i+1)*(i+1))

# print(nums)

nums=[((i+1)*(i+1)) for i in range(n)]
print(nums)