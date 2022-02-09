# 크로아티아 알파벳

Cra = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
al = input()

for i in Cra:
    al = al.replace(i,'`')

print(len(al))