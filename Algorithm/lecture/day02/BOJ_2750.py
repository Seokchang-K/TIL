# 수 정렬하기

T = int(input())

numbers = [int(input()) for _ in range(T)]
sort_num = sorted(numbers)

# for i in sort:
#     print(i)
print(*sort_num, sep='\n')

# 다른 풀이

# n = int(input())
# numbers = [int(input())for _ in range(n)]
# sorted_numbers = sorted(numbers)

# print(*sorted_numbers, sep='\n')
# print(*sorted(numbers), sep='\n')
# print(*sorted([int(input())for _ in range(n)]), sep='\n')
# print(*sorted([int(input())for _ in range(int(input()))]), sep='\n')
# 줄여버리기

