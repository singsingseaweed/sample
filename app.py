import streamlit as st
import math

def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
    # 각 개인의 시간에 따른 분배 비율 계산
    distribution_ratio = [hours / total_hours_worked for hours in hours_worked]
    
    # 각 개인의 분배 금액 계산
    individual_incomes = [round(ratio * total_income) for ratio in distribution_ratio]
    
    # 남은 잔돈 계산
    remaining_change = total_income - sum(individual_incomes)
    
    return individual_incomes, remaining_change

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
    individual_incomes, remaining_change = distribute_money(hours_worked, total_income)

    # 결과 출력
    st.write("개인별 분배된 돈:")
    for i, income in enumerate(individual_incomes):
        st.write(f"개인 {i+1}: {income}원")
    
    # 잔돈 출력
    if remaining_change > 0:
        st.write(f"잔돈: {remaining_change}원")
    elif remaining_change < 0:
        st.write("잔돈이 마이너스입니다. 입력값을 확인하세요.")
    else:
        st.write("잔돈이 없습니다.")
