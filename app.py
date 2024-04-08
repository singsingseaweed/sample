import streamlit as st
import math

def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
    # 각 개인의 분배 금액 계산
    individual_incomes = []
    for hours in hours_worked:
        # 최소 요금 계산
        minimum_payment = (total_income / total_people) / 2
        # 즐긴 시간에 따른 분배 금액 계산
        income = max(minimum_payment, minimum_payment * (hours / total_hours_worked))
        individual_incomes.append(income)
    
    # 남은 잔돈 계산
    remaining_change = total_income - sum(individual_incomes)
    
    return individual_incomes, remaining_change

# Streamlit 애플리케이션 제목 설정
st.title("시간으로 금액분배")

# 각 개인의 정보 입력 받기
num_people = st.number_input("전체 참여인원", min_value=1, step=1, value=1)
hours_worked = st.number_input("회식한 시간", min_value=0, step=1)

# 도망간 사람들의 수 입력 받기
num_runaway = st.number_input("중간 귀가자들", min_value=0, step=1)

# 각 도망간 사람들의 정보 입력 받기
runaway_hours = []
for i in range(num_runaway):
    runaway_hours.append(st.number_input(f"{i+1}번째 귀가한 사람의 즐긴 시간", min_value=0, step=1))

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 유효성 검사
    if total_income <= 0 or num_people <= num_runaway or hours_worked <= 0 or any(hour < 0 for hour in runaway_hours):
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        total_working_hours = (num_people - num_runaway) * hours_worked + sum(runaway_hours)
        individual_hours = [hours_worked] * (num_people - num_runaway) + runaway_hours
        
        # 분배된 돈 계산
        individual_incomes, remaining_change = distribute_money(individual_hours, total_income)

        # 결과 출력
        st.write("분배된 돈:")
        for i in range(len(individual_incomes)):
            st.write(f"사람 {i+1}: {individual_incomes[i]:,.0f}원")
        
        # 잔돈 출력
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
