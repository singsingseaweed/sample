import streamlit as st
import math

def distribute_money(hours_worked_full, hours_worked_runaway, total_income):
    total_hours_worked = sum(hours_worked_full)
    total_people_full = len(hours_worked_full)
    total_people_runaway = len(hours_worked_runaway)
    
    # 각 개인의 시간에 따른 분배 비율 계산
    distribution_ratio_full = [hours / total_hours_worked for hours in hours_worked_full]
    distribution_ratio_runaway = [hours / total_hours_worked for hours in hours_worked_runaway]
    
    # 각 개인의 분배 금액 계산 (끝까지 일한 인원)
    individual_incomes_full = [ratio * total_income for ratio in distribution_ratio_full]
    
    # 각 개인에게 분배된 돈을 100단위로 떨어지도록 조정 (끝까지 일한 인원)
    rounded_incomes_full = [math.floor(income / 100) * 100 for income in individual_incomes_full]
    
    # 각 개인에게 분배된 돈을 100단위로 떨어지도록 조정 (중간에 도망친 인원)
    individual_incomes_runaway = [ratio * total_income for ratio in distribution_ratio_runaway]
    rounded_incomes_runaway = [math.floor(income / 100) * 100 for income in individual_incomes_runaway]
    
    # 남은 잔돈 계산
    remaining_change_full = total_income - sum(rounded_incomes_full)
    remaining_change_runaway = total_income - sum(rounded_incomes_runaway)
    
    return rounded_incomes_full, remaining_change_full, rounded_incomes_runaway, remaining_change_runaway

# Streamlit 애플리케이션 제목 설정
st.title("돈을 공정하게 분배해주는 앱")

# 끝까지 일한 인원의 정보 입력 받기
num_people_full = st.number_input("끝까지 일한 사람의 수를 입력하세요", min_value=0, step=1, value=0)

hours_worked_full = []
for i in range(num_people_full):
    hours_worked_full.append(st.number_input(f"끝까지 일한 {i+1}번째 사람의 일한 시간을 입력하세요", min_value=0, step=1))

# 중간에 도망간 인원의 정보 입력 받기
num_people_runaway = st.number_input("중간에 도망간 사람의 수를 입력하세요", min_value=0, step=1, value=0)

hours_worked_runaway = []
for i in range(num_people_runaway):
    hours_worked_runaway.append(st.number_input(f"중간에 도망간 {i+1}번째 사람의 일한 시간을 입력하세요", min_value=0, step=1))

# 전체 수익 입력 받기
total_income = st.number_input("전체 수익을 입력하세요", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 분배된 돈 계산
    rounded_incomes_full, remaining_change_full, rounded_incomes_runaway, remaining_change_runaway = distribute_money(hours_worked_full, hours_worked_runaway, total_income)

    # 결과 출력 (끝까지 일한 인원)
    st.write("끝까지 일한 사람들의 분배된 돈:")
    for i, income in enumerate(rounded_incomes_full):
        st.write(f"개인 {i+1}: {income:.2f}원")
    if remaining_change_full > 0:
        st.write(f"잔돈 (끝까지 일한 인원): {remaining_change_full:.2f}원")
    
    # 결과 출력 (중간에 도망간 인원)
    st.write("중간에 도망간 사람들의 분배된 돈:")
    for i, income in enumerate(rounded_incomes_runaway):
        st.write(f"개인 {i+1}: {income:.2f}원")
    if remaining_change_runaway > 0:
        st.write(f"잔돈 (중간에 도망간 인원): {remaining_change_runaway:.2f}원")
