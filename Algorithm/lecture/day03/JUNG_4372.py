# 945 : 기타 자료형 - 자가진단 5

# 딕셔너리 만들기
ani = {
    "Pokemon":"Pikachu",
    "Digimon":"Agumon",
    "Yugioh":"Black Magician"
}

# word = input()

# 세 개중에 나오면 value/I don't know

# if word in ani:
#     print(ani[word])
# else:
#     print("I don't know")

print(ani.get(input(), "I don't know"))