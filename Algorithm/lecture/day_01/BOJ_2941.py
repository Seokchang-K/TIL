# 크로아티아 알파벳

Cra = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
al = input()

for i in Cra:
    al = al.replace(i,'`')

print(len(al))

# 다른 풀이

# word = input()
# changes = ['=', '-', 'lj', 'nj', 'dz=']
# total = len(word)

# for i in changes:
#     total -= word.count(i)
# print(total)