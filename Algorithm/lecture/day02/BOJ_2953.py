# 나는 요리사다

competive = [sum(list(map(int,input().split()))) for _ in range(5)]
competive.index(max(competive))
print(int(competive.index(max(competive)))+1, max(competive))