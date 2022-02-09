# A+B - 8
T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")

# 관례상 '_' 는 사용하지 않는 변수에 할당되는 문자이기에 사용할 변수에는 쓰지 않는 것이 좋다.
