import streamlit as st
import math

def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
    # 각 개인의 분배 비율 계산
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

# 각 개인의 정보 입력 받기
num_people = st.number_input("전체 인원 수를 입력하세요", min_value=1, step=1, value=1)
hours_worked = st.number_input("일한 시간을 입력하세요", min_value=0, step=1)

# 도망간 사람들의 수 입력 받기
num_runaway = st.number_input("도망간 사람의 수를 입력하세요", min_value=0, step=1)

# 각 도망간 사람들의 정보 입력 받기
runaway_hours = []
for i in range(num_runaway):
    runaway_hours.append(st.number_input(f"{i+1}번째 도망간 사람의 일한 시간을 입력하세요", min_value=0, step=1))

# 전체 수익 입력 받기
total_income = st.number_input("전체 수익을 입력하세요", min_value=0)

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
        result = {}
        for i, income in enumerate(individual_incomes):
            if individual_hours[i] not in result:
                result[individual_hours[i]] = income
        
        st.write("일한 시간별 분배된 돈:")
        for hours, income in result.items():
            st.write(f"{hours}시간을 일한 사람들: {income:,.0f}원")
        
        # 잔돈 출력
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
