# 946:기타 자료형 - 자가진단 6

n = int(input())
countrys = {}

for _ in range(n):
    k, v = input().split()
    countrys[k] = v
    
x = input()

print(countrys.get(x,'Unknown Country'))