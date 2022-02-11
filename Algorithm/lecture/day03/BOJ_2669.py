# 직사각형 네개의 합집합의 면적 구하기

# paper = [[0]*100 for _ in range(100)]

# for _ in range(4):
#     x,z,y,r = map(int,input().split())
#     for i in range(x,y):
#         for j in range(z,r):
#             paper[i][j] = 1
# total = 0
# for i in range(100):
#     for j in range(100):
#         total += paper[i][j]

# print(total)


plate = [[0]*100 for _ in range(100)]

for _ in range (4):
    x,z,y,r = map(int,input().split())
    for i in range(x,y):
        for j in range(z,r):
            plate[i][j] = 1

squar = 0

for i in range(100):
    for j in range(100):
        squar += plate[i][j]

print(squar)