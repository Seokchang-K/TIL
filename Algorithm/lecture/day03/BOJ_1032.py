# 명령 프롬프트

n = int(input())
fw = list(input())
lfw = len(fw)

for _ in range(n-1):
    words = list(input())
    for i in range(lfw):
        if fw[i] != words[i]:
            fw[i] = '?'
print(''.join(fw))