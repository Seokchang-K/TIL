# 별 찍기 - 20

T = int(input())

for i in range(T):
    if i % 2 == 0:
        print('* ' * T)
    else:
        print(' *' * T)

# in 1 line

# for i in range(T):
#     print('* '* T if i % 2 == 0 else ' *' * T)
# list comprehension