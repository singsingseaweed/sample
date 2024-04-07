import streamlit as st

def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
    # 각 개인의 시간에 따른 분배 비율 계산
    distribution_ratio = [hours / total_hours_worked for hours in hours_worked]
    
    # 각 개인의 분배 금액 계산
    individual_incomes = [ratio * total_income for ratio in distribution_ratio]
    
    return individual_incomes

# Streamlit 애플리케이션 제목 설정
st.title("돈을 공정하게 분배해주는 앱")

# 각 개인의 정보 입력 받기
num_people = st.number_input("일한 사람의 수를 입력하세요", min_value=1, step=1, value=1)

hours_worked = []
for i in range(num_people):
    hours_worked.append(st.number_input(f"{i+1}번째 사람의 일한 시간을 입력하세요", min_value=0, step=1))

# 전체 수익 입력 받기
total_income = st.number_input("전체 수익을 입력하세요", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 분배된 돈 계산
    individual_incomes = distribute_money(hours_worked, total_income)

    # 결과 출력
    st.write("개인별 분배된 돈:")
    for i, income in enumerate(individual_incomes):
        st.write(f"개인 {i+1}: {income:.2f}원")
