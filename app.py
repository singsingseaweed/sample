import streamlit as st

def calculate_payment(start_times, end_times):
    total_time = 0
    for start, end in zip(start_times, end_times):
        total_time += (end - start).total_seconds() / 3600  # 시간을 시간 단위로 변환하여 총 시간을 계산

    num_people = len(start_times)
    payments = [0] * num_people

    for i in range(num_people):
        for start, end in zip(start_times, end_times):
            shared_time = min(end, end_times[i]) - max(start, start_times[i])
            if shared_time > 0:
                payments[i] += shared_time.total_seconds() / 3600 / total_time  # 시간 비율에 따라 지불 금액 계산

    return [payment * total_bill for payment in payments]

def main():
    st.title("회식 비용 분배기")

    total_bill = st.number_input("총 결제 금액을 입력하세요:", value=0.0, step=0.01)
    num_people = st.number_input("참석자 수를 입력하세요:", min_value=1, value=1, step=1)

    start_times = []
    end_times = []

    for i in range(int(num_people)):
        st.subheader(f"참석자 {i + 1}의 시작 및 종료 시간을 입력하세요:")
        start_time = st.time_input("시작 시간:")
        end_time = st.time_input("종료 시간:")
        start_times.append(start_time)
        end_times.append(end_time)

    payments = calculate_payment(start_times, end_times)

    st.write("\n결제할 금액:")
    for i, payment in enumerate(payments):
        st.write(f"참석자 {i + 1}: {payment:.2f} 원")

if __name__ == "__main__":
    main()
