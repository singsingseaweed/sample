import streamlit as st
import math

def distribute_money(hours_per_group, total_income):
    total_hours_worked = sum(hours_per_group)
    total_people = sum(len(group) for group in hours_per_group)
    
    # 각 그룹의 시간에 따른 분배 비율 계산
    distribution_ratio = [sum(group) / total_hours_worked for group in hours_per_group]
    
    # 각 그룹의 분배 금액 계산
    group_incomes = [ratio * total_income for ratio in distribution_ratio]
    
    # 각 그룹에게 분배된 돈을 100단위로 떨어지도록 조정
    rounded_incomes = [math.floor(income / 100) * 100 for income in group_incomes]
    
    # 남은 잔돈 계산
    remaining_change = total_income - sum(rounded_incomes)
    
    return rounded_incomes, remaining_change

# Streamlit 애플리케이션 제목 설정
st.title("돈을 공정하게 분배해주는 앱")

# 각 그룹의 정보 입력 받기
num_groups = st.number_input("그룹의 수를 입력하세요", min_value=1, step=1, value=1)

hours_per_group = []
for i in range(num_groups):
    group_hours = st.number_input(f"{i+1}번째 그룹의 일한 시간을 입력하세요", min_value=0, step=1)
    hours_per_group.append([group_hours])

# 전체 수익 입력 받기
total_income = st.number_input("전체 수익을 입력하세요", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 분배된 돈 계산
    group_incomes, remaining_change = distribute_money(hours_per_group, total_income)

    # 결과 출력
    st.write("그룹별 분배된 돈:")
    for i, income in enumerate(group_incomes):
        st.write(f"그룹 {i+1}: {income:.2f}원")
    
    # 잔돈 출력
    if remaining_change > 0:
        st.write(f"잔돈: {remaining_change:.2f}원")
