# 이탈하지 않은 사람들의 회식시간 입력 받기
default_hours = st.number_input("이탈하지 않은 사람들의 회식한 시간", min_value=0, step=1)

# 중간에 이탈한 사람의 수 입력 받기
num_quitters = st.number_input("중간에 이탈한 사람의 수", min_value=0, max_value=num_people-1, step=1, value=0)

# 이탈한 사람들의 회식시간 입력 받기
quitter_hours = []
for i in range(num_quitters):
    quitter_hours.append(st.number_input(f"{i+1}번째 이탈한 사람의 회식한 시간", min_value=0, step=1))

# 전체 수익 입력 받기
total_income = st.number_input("총 금액", min_value=0)

# "분배하기" 버튼 클릭 시 실행되는 코드
if st.button("분배하기"):
    # 이탈한 사람들의 수와 회의시간을 포함하여 모든 회의시간을 결합
    hours_worked = [default_hours] * (num_people - num_quitters) + quitter_hours
    
    # 유효성 검사
    if total_income <= 0 or any(hour < 0 for hour in hours_worked):
        st.error("잘못된 입력입니다.")
    else:
        # 각 개인이 받아야 할 돈 계산
        individual_incomes, remaining_change = distribute_money(hours_worked, total_income)

        # 결과 그룹화
        grouped_results = {}
        for i, income in enumerate(individual_incomes):
            if income not in grouped_results:
                grouped_results[income] = []
            grouped_results[income].append(i + 1)

        # 그룹별 결과 출력
        for income, participants in grouped_results.items():
            participant_str = ', '.join([str(participant) for participant in participants])
            st.write(f"{len(participants)}시간 참여인들: {income:,.0f}원")

        # 잔돈 출력
        if remaining_change > 0:
            st.write(f"잔돈: {remaining_change:,.0f}원")
        elif remaining_change < 0:
            st.write(f"잔돈: {-remaining_change:,.0f}원 부족")
