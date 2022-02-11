# 숫자의 합

_ = input()
numbers = list(map(int,input()))
total = 0

for i in numbers:
    total += i

print(total)

# 다른 방법

# _ = input()

# total = sum(map(int,input()))
# print(total)