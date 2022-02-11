# 953:기타 자료형 - 형성평가 6

players = list(input().split())
pauls={}

for player in players:
    pauls[player]=(players.count(player))
    
m_p = min(pauls.values())

for player, paul in pauls.items():    
  if paul == m_p:
      print(player)

print(m_p)


# 정답

# players = input().split()
# fouls = {}

# for player in players:
#     # 이미 파울을 했니?
#     if player in fouls:
#         fouls[player] += 1
    
#     # 파울 한번도 안했었니?
#     else:
#         fouls[player] = 1

# # 파울 가장 적게한 선수 뽑기
# min_foul = min(fouls.values())

# for player, foul in fouls.items():
#     if foul == min_foul:
#         print(player)
# print(min_foul)