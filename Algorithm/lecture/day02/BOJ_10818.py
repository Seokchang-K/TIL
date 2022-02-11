# 최소, 최대

n = input()

numbers = list(map(int, input().split()))
min_n = min(numbers)
max_n = max(numbers)

print(min_n, max_n)

# 다른 방법

# n = input()
# numbers = list(map(int, input().split()))
# print(min(numbers), max(numbers))