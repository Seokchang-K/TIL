# 별 찍기 - 2

T = int(input())

for i in range(T):
    print(((i+1) * '*').rjust(T))

# 선생님 풀이
# T = int(input())

# for i in range(T):
#     print(' ' * (T-i-1) + '*' * (i + 1))