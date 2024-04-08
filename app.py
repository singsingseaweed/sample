import streamlit as st
import math

# 시간에 따라 분배하는 함수
def distribute_money(hours_worked, total_income):
    total_hours_worked = sum(hours_worked)
    total_people = len(hours_worked)
    
    # 모든 사람의 즐긴 시간을 통일
    unified_hours = total_hours_worked / total_people
    
    # 중간 귀가자들의 수
    num_runaway = total_people - 1
    
    # 최소 금액 계산
    min_amount_per_person = total_income / (2 * total_people)
    
    # 최소 금액을 중간 귀가자들에게 적용
    min_amount_runaway = min_amount_per_person * num_runaway
    
    # 최소 금액을 나눈 나머지 금액 계산
    remaining_amount = total_income - min_amount_runaway
    
    # 중간 귀가자들의 즐긴 시간에 따른 비율 계산
    distribution_ratio = [(unified_hours - hour) / (total_hours_worked - unified_hours * num_runaway) for hour in hours_worked]
    
    # 중간 귀가자들에게 분배된 돈 계산
    individual_incomes = [min_amount_per_person] * num_runaway
    
    # 남은 금액을 시간당 비율에 따라 배분
    for i in range(num_runaway):
        individual_incomes[i] += remaining_amount * distribution_ratio[i]
    
    # 각 개인에게 분배된 돈을 100단위로 떨어지도록 조정
    rounded_incomes = [math.floor(income / 100) * 100 for income in individual_incomes]
    
    # 남은 잔돈 계산
    remaining_change = total_income - sum(rounded_incomes)
    
    return rounded_incomes, remaining_change

# Streamlit 애플리케이션 제목 설정
st.title("시간으로 금액분배")

# 전체 참여인원 입력 받기
num_people = st.number_input("전체 참여인원", min_value=2, step=1, value=2)

# 모든 사람의 즐긴 시간 입력 받기
hours_worked = st.number_input("모든 사람의 즐긴 시간", min_value=0, step=1)

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 유효성 검사
    if total_income <= 0 or hours_worked <= 0:
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        individual_incomes, remaining_change = distribute_money([hours_worked] * num_people, total_income)

        # 결과 출력
        st.write("분배된 돈:")
        for i, income in enumerate(individual_incomes):
            st.write(f"{i+1}번째 참여인: {income:,.0f}원")

        # 잔돈 출력
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
