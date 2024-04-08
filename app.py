import streamlit as st

# Streamlit 애플리케이션 제목 설정
st.title("회식 비용 분배기")

# 회식한 총 시간 입력 받기
total_hours = st.number_input("회식한 총 시간", min_value=0, step=1)

# 각 개인의 정보 입력 받기
num_people = st.number_input("전체 참여인원", min_value=1, step=1, value=1)
people_data = []
for i in range(num_people):
    person_hours = st.number_input(f"{i+1}번째 참여인의 회식한 시간", min_value=0, step=1)
    people_data.append({"hours": person_hours, "amount_paid": None})

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 유효성 검사
    if total_income <= 0:
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        total_hours_worked = sum(person["hours"] for person in people_data)
        individual_incomes = []
        remaining_amount = total_income
        for person in people_data:
            if total_hours_worked > 0:
                individual_hours_ratio = person["hours"] / total_hours_worked
            else:
                individual_hours_ratio = 1 / num_people
            individual_payment = individual_hours_ratio * total_income
            person["amount_paid"] = st.number_input(f"지불할 금액 (참여인 {people_data.index(person)+1})", value=individual_payment, min_value=0)
            individual_incomes.append(person["amount_paid"])

        # 결과 출력
        for i, income in enumerate(individual_incomes):
            st.write(f"{i+1}번째 참여인: {income:,.0f}원")

        # 남은 잔돈 계산
        remaining_change = total_income - sum(individual_incomes)
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
