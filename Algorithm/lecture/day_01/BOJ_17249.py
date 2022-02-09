# 태보태보 총 난타
Tae = input()

La = Tae[:int(Tae.find('(^0^)'))].count('@')
Ra = Tae[int(Tae.find('(^0^)')):].count('@')

print(La, Ra, sep=' ')

# 다른 풀이.

# left, right = input().split('0')
# print(left.count('@'), right,count('@'))