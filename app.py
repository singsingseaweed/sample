import streamlit as st
import math

# 시간에 따라 분배하는 함수
def distribute_money(hours_worked, total_income):
    total_people = len(hours_worked)
    
    # 모든 사람에게 동일한 시간을 적용
    total_hours_worked = sum(hours_worked)
    
    # 각 개인의 분배 비율 계산
    distribution_ratio = [hours / total_hours_worked for hours in hours_worked]
    
    # 최소 금액 계산
    min_amount_per_person = total_income / (2 * total_people)
    
    # 최소 금액을 각 개인에게 적용
    individual_incomes = [min_amount_per_person] * total_people
    
    # 남은 금액 계산
    remaining_amount = total_income - min_amount_per_person * total_people
    
    # 남은 금액을 시간당 비율에 따라 배분
    for i in range(total_people):
        individual_incomes[i] += remaining_amount * distribution_ratio[i]
    
    # 각 개인에게 분배된 돈을 100단위로 떨어지도록 조정
    rounded_incomes = [math.floor(income / 100) * 100 for income in individual_incomes]
    
    # 남은 잔돈 계산
    remaining_change = total_income - sum(rounded_incomes)
    
    return rounded_incomes, remaining_change

# Streamlit 애플리케이션 제목 설정
st.title("시간으로 금액분배")

# 회식한 총 시간 입력 받기
total_hours = st.number_input("회식한 총 시간", min_value=0, step=1)

# 각 개인의 정보 입력 받기
num_people = st.number_input("전체 참여인원", min_value=1, step=1, value=1)

# 이탈한 사람의 수 입력 받기
num_dropout = st.number_input("회식에서 이탈한 사람 수", min_value=0, step=1, value=0)

# 이탈한 사람의 시간을 제외한 총 시간 계산
total_hours_excluding_dropout = total_hours - sum(st.number_input(f"{i+1}번째 이탈한 사람의 회식한 시간", min_value=0, step=1) for i in range(num_dropout))

hours_worked = [total_hours_excluding_dropout] * (num_people - num_dropout)  # 이탈한 사람의 수를 제외한 인원에게 동일한 시간 적용

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 유효성 검사
    if total_income <= 0:
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        individual_incomes, remaining_change = distribute_money(hours_worked, total_income)

        # 결과 출력
        for i, income in enumerate(individual_incomes):
            st.write(f"{i+1}번째 참여인: {income:,.0f}원")

        # 잔돈 출력
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
