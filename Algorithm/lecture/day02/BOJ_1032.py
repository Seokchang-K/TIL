# 명령 프롬프트

n = int(input())
fw = list(input())
lfw = len(fw)

for i in range(n-1):
    word = list(input())
    for j in range(lfw):
        if fw[j] != word[j]:
            fw[j] = '?'

print(''.join(fw))