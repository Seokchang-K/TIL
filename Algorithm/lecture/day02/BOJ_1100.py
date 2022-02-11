# 하얀 칸

chase_plate = []

for i in range(8):
    slot = list(input())
    if i % 2 == 0:
        chase_plate.extend(slot[::2])
    else:
        chase_plate.extend(slot[1::2])
    
print(chase_plate.count('F'))

# print(sum(input()[i % 2 :: 2].count('F') for i in range(8)))

# 선생님 풀이

# board = [list(input()) for _ in range(8)]
# total = 0

# for i in range(8):
#     for j in range(8):
#         if i % 2 == j % 2 and board[i][j] == "F":
#             # 여기서 board[j][i]로 바꿔주면 가로가 아닌 세로로 탐색한다.
#             total += 1

# print(total)