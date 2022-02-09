# 오타맨 고창영

Leng = int(input())

for _ in range(Leng):
    n, w = input().split()
    word = w[:int(n)-1]+w[int(n):]

    print(word)

# 다른 풀이
# for _ in range(int(input())):
#     index, word = input().split()
#     index = int(index)
#     print(word[:index - 1] + word[index:])