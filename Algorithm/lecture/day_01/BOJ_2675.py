# 문자열 반복

T = int(input())

for _ in range(T):
    rep, word = input().split()
    for i in word:
        print(i * int(rep), end='')
    print()
