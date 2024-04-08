import streamlit as st
import math

# 시간에 따라 분배하는 함수
def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
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

# 각 개인의 정보 입력 받기
num_people = st.number_input("전체 참여인원", min_value=1, step=1, value=1)
total_hours = st.number_input("전체 회식 시간", min_value=0)

# 중간이탈자들의 회의 시간 입력 받기
dropout_hours = []
for i in range(num_people):
    dropout_hours.append(st.number_input(f"{i+1}번째 중간이탈자의 회식 시간", min_value=0, step=1))

# 중간이탈자를 제외한 나머지 회식 시간 계산
remaining_people_hours = total_hours - sum(dropout_hours)

# 나머지 참여자의 회식 시간 입력 받기
remaining_hours = [st.number_input(f"{i+1}번째 참여인의 회식 시간", min_value=0, step=1, value=remaining_people_hours / (num_people - len(dropout_hours))) for i in range(num_people - len(dropout_hours))]

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 유효성 검사
    if total_income <= 0 or any(hour < 0 for hour in dropout_hours + remaining_hours):
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        hours_worked = dropout_hours + remaining_hours
        individual_incomes, remaining_change = distribute_money(hours_worked, total_income)

        # 결과 출력
        for i, income in enumerate(individual_incomes):
            st.write(f"{i+1}번째 참여인: {income:,.0f}원")

        # 잔돈 출력
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
