# 평균은 넘겠지

c = int(input())

for _ in range(c):
    numbers = list(map(int,input().split()))
    # 여러 줄에 걸쳐서 데이터를 받아 오기 위해서 range(c) 범위의 for문 안에서 받아온다.
    # c번 만큼 반복하는 for 문으로 인해 c 번 만큼 데이터를 받아온다
    avg = sum(numbers[1:])/numbers[0]
    # 일단 먼저 학생들의 점수를 평균내는데 리스트로 받은 성적들은 인덱스[1] 부터 시작된다
    # 학생들의 숫자는 리스트의 0번째 이다.
    # 평균을 -> 학생들의 성적합(sum(numbers[1:]))/학생수[0]
    count_m = 0
    # 평균을 넘긴 학생들의 숫자를 새기위해서 0객체가 할당된 변수 지정.
    for score in numbers[1:]:
        if score > avg:
            # 평균을 넘긴 학생을 numbers 리스트의 각요소 score 와 평균을 비교
            count_m += 1
            # 평균넘긴 학생수를 센다.

    rate = count_m/numbers[0] * 100
    # 비율을 구하기위해서 평균넘긴 학생수를 학생수인 number[0]으로 나눈다
    # 백분율로 구하기 위해서 100 을 곱해준다.
    print(f'{rate:.3f}%')
    # 포멧팅을 위해서 f를 쓰고 소수점 셋째 자리로 내기 위해서 .3f 를 써준다.
