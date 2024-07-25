# 회원 정보를 입력 받아 출력 하기
# 이름 입력
# 나이 입력 : 1~199까지, 틀리면 재 입력 요구
# 성별 입력 : m/M, f/F, 나머지는 재 입력 요구
# 직업 입력 : 1,2,3,4 나머지는 재 입력 요구
# 결과를 마지막에 출력
def input_age():
    while True:
        age = input("나이를 입력: ")
        if age.isdigit(): # 문자열이 숫자로 구성되어 있는지 확인
            age = int(age)
            if 0 < age < 200: return age
        print("나이를 잘못 입력 했습니다.")

def input_gender():
    while True:
        gender = input("성별 입력: ")
        if gender.lower() == "m": return "남성"
        elif gender.lower() == "f": return "여성"
        print("성별을 잘못 입력 했습니다.")

def input_jobs():
    while True:
        jobs = input("직업을 입력: ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘못 입력 했습니다.")

# [] 리스트, {} 딕셔너리, () 튜플
def print_info(name, age, gender, jobs):
    jobs_str = "", "학생", "회사원", "주부", "무직" # 튜플 :
    print("="*3, "회원정보", "="*3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"


# 함수 호출과 파일 저장하기
fd = open("member.txt", "wt", encoding="utf-8")
while True:
    name = input("이름 입력 / 종료는 quit : ")
    if name == "quit": break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name, age, gender, jobs)
    fd.write(rst + "\n")
fd.close()