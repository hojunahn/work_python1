# 조건문과 반복문은 제어문이라하고, 이는 순차적인 흐름을 제어하는 목적으로 사용
# 파이썬의 조건문 자바의 if문과 switch문을 결합한 형태와 유사하며, 파이썬은 switch문 없음
# 조건문의 수행은 들여쓰기 구분하고 각각의 조건은 :(클론)으로 구분
# num = int(input("정수를 입력 : "))
#
# if num > 100:
#     print("입력 값이 100보다 큽니다.")
# elif num < 100:
#     print("입력 값이 100보다 작습니다.")
# else:
#     print("입력 값이 100과 같습니다.")

# season = input("지금 계절은 ? > ")
#
# if season == "spring":
#     print("따뜻한 봄입니다.")
# elif season == "summer":
#     print("무더운 여름입니다.")
# elif season == "fall" or season == "autumn":
#     print("쓸쓸한 가을입니다.")
# else:
#     print("추운 겨울입니다.")

# 성적에 대한 학점 출력하기
# 국어, 영어, 수학 성적을 입력 받아 평균을 구해 등급 출력하기
# 평균이 90이상 A, 80이상 B, 70이상 C, 60이상 D, 나머지는 F

score = list(map(int,input("국어,영어,수학 점수 입력 : ").split()))

num = sum(score)/len(score)

if num >= 90:
    print("등급 : A")
elif num >= 80:
    print("등급 : B")
elif num >= 70:
    print("등급 : C")
elif num >= 60:
    print("등급 : D")
else:
    print("등급 : F")

print(f"평균은 {num:.2f}점 입니다.")