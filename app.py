import streamlit as st
import math

def distribute_money(total_income, num_people):
    # 최소 분배 금액 계산
    min_income_per_person = total_income / (2 * num_people)
    
    # 각 개인에게 분배된 돈 계산
    individual_incomes = [min_income_per_person + (total_income - min_income_per_person * 2 * num_people) / num_people] * num_people
    
    return individual_incomes

# Streamlit 애플리케이션 제목 설정
st.title("시간으로 금액분배")

# 전체 참여인원 입력 받기
num_people = st.number_input("전체 참여인원", min_value=1, step=1, value=1)

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 유효성 검사
    if total_income <= 0 or num_people <= 0:
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        individual_incomes = distribute_money(total_income, num_people)

        # 결과 출력
        st.write("개인별 분배된 돈:")
        for i, income in enumerate(individual_incomes):
            st.write(f"{i+1}번째 사람: {income:,.0f}원")
