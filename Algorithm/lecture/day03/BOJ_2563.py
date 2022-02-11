# 색종이 구하기.

# 0으로 이루어진 도화지를 만든다.
paper = [[0]*100 for _ in range(100)]

# 색종이의 갯수
n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            # 도화지가 빈칸이면
            # if paper[i][j] == 0:
                # paper[i][j] == 1 # 색칠
                # 굳이 0일때만 1변환 할 필요 없이 1이 있으면 그냥 지나친다.
            paper[i][j] = 1
# 영역의 넓이 출력(도화지에서 1인 부분을 그냥 다 더한다)
total = 0
for i in range(100):
    for j in range(100):
        total += paper[i][j]

# total = sum(sum(line) for line in paper)

print(total)
