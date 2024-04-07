import streamlit as st
import math

def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
    # 각 개인의 시간에 따른 분배 비율 계산
    distribution_ratio = [hours / total_hours_worked for hours in hours_worked]
    
    # 각 개인의 분배 금액 계산
    individual_incomes = [ratio * total_income for ratio in distribution_ratio]
    
    # 각 개인에게 분배된 돈을 100단위로 떨어지도록 조정
    rounded_incomes = [math.floor(income / 100) * 100 for income in individual_incomes]
    
    # 남은 잔돈 계산
    remaining_change = total_income - sum(rounded_incomes)
    
    return rounded_incomes, remaining_change

# Streamlit 애플리케이션 제목 설정
st.title("돈을 공정하게 분배해주는 앱")

# 전체 인원 수 입력 받기
total_people = st.number_input("전체 인원 수를 입력하세요", min_value=1, step=1, value=1)

# 최대 일한 시간 설정
max_hours_worked = st.number_input("모든 사람이 최대로 일한 시간을 입력하세요", min_value=1, step=1, value=8)

# 먼저 집에간 그룹의 정보 입력 받기
num_group1 = st.number_input("먼저 집에 간 그룹의 사람 수를 입력하세요", min_value=0, step=1, value=0)
group1_hours_worked = st.number_input("먼저 집에 간 그룹의 총 일한 시간을 입력하세요", min_value=0, step=1, value=0)

# 두 번째로 집에간 그룹의 정보 입력 받기
num_group2 = st.number_input("그 다음 집에 간 그룹의 사람 수를 입력하세요", min_value=0, step=1, value=0)
group2_hours_worked = st.number_input("그 다음 집에 간 그룹의 총 일한 시간을 입력하세요", min_value=0, step=1, value=0)

# 세 번째로 집에간 그룹의 정보 입력 받기
num_group3 = st.number_input("마지막으로 집에 간 그룹의 사람 수를 입력하세요", min_value=0, step=1, value=0)
group3_hours_worked = st.number_input("마지막으로 집에 간 그룹의 총 일한 시간을 입력하세요", min_value=0, step=1, value=0)

# 전체 수익 입력 받기
total_income = st.number_input("전체 수익을 입력하세요", min_value=0)

# 각 그룹의 총 일한 시간 계산
total_group_hours_worked = group1_hours_worked + group2_hours_worked + group3_hours_worked

# 모든 사람들의 총 일한 시간 계산
total_hours_worked = max(max_hours_worked, total_group_hours_worked)

# 모든 그룹에 속한 사람들의 일한 시간 계산
hours_worked = [total_hours_worked] * num_group1 + [total_hours_worked] * num_group2 + [total_hours_worked] * num_group3

# 나머지 그룹에 속한 사람들의 수 계산
num_remaining_people = total_people - num_group1 - num_group2 - num_group3

# 모든 그룹에 속하지 않은 사람들의 일한 시간 계산
hours_worked += [total_hours_worked] * num_remaining_people

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 분배된 돈 계산
    individual_incomes, remaining_change = distribute_money(hours_worked, total_income)

    # 결과 출력
    st.write("개인별 분배된 돈:")
    for i, income in enumerate(individual_incomes):
        st.write(f"개인 {i+1}: {income:.2f}원")
    
    # 잔돈 출력
    if remaining_change > 0:
        st.write(f"잔돈: {remaining_change:.2f}원")
