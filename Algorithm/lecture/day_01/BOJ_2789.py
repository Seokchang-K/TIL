# 유학 금지

cam = 'CAMBRIDGE'
word = input()

for i in list(cam):
    word = word.replace(i,'')
    # 원문을 지워야 안에 있는 다른 글자도 지울 수 있기 때문에 원문을 변조하게끔 원문 변수를 다시 써주자.

print(word)

# 선생님 풀이

# word = input()

# for i in 'CAMBRIDGE':
#     word = word.replace(i, '')

# print(word)