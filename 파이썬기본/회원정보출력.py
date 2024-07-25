# 입력칸
name = input("이름 입력: ")
age = int(input("나이 입력(1<age<199): "))
gender = input("성별 입력(m/f): ")
jobs = int(input("직업 입력 [1:학생] [2:회사원] [3:주부] [4:무직]: "))

# 나이 제한
if not (1<age<199):
    print("나이를 재입력 해주세요.")
    exit()

# 성별
if gender.lower() == "m":
    gd_box = "남성"
elif gender.lower() == "h":
    gd_box = "여성"
else:
    print("성별을 재입력 해주세요")
    exit()

# 직업
if jobs == 1:
    jb_box = "학생"
elif jobs == 2:
    jb_box = "회사원"
elif jobs == 3:
    jb_box = "주부"
elif jobs == 4:
    jb_box = "무직"
else:
    print("직업을 재입력 해주세요.")
    exit()

print(f"이름:{name} 나이:{age} 성별:{gd_box} 직업:{jb_box}")