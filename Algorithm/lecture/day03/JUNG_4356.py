n = int(input())

# a = ['No.'+ str(i) for i in range(1, n + 1)]
a = [f'No.{i}' for i in range(1, n + 1)]
# 이렇게 f 포멧팅 하는게 제일 강력하고 빠르다!
# a = ['No.'+ str(i) for i in range(1, int(input())+1)]

print(a)