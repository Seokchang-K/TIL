# 팰린드롬인지 확인하기

a = input()

if a == a[::-1]:
    print(1)
else:
    print(0)

# 다른 방법

# word = input()

# print(1 if word == word[::-1] else 0)

# print(int(word == word[::-1]))
# 불리언 형식으로 나온것을 int로 바꿔서 프린트 해주었다.