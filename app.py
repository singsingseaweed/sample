def calculate_payment(num_people, total_bill, time_spent):
    total_time = sum(time_spent)
    payments = []

    for i in range(num_people):
        share = total_bill * (time_spent[i] / total_time)
        payments.append(share)

    return payments

def main():
    num_people = 20
    total_bill = float(input("총 결제 금액을 입력하세요: "))
    time_spent = []

    print("각 사람이 머문 시간을 입력하세요:")
    for i in range(num_people):
        time = float(input("사람 {}의 머문 시간: ".format(i+1)))
        time_spent.append(time)

    payments = calculate_payment(num_people, total_bill, time_spent)

    print("\n결제할 금액:")
    for i, payment in enumerate(payments):
        print("사람 {}: {:.2f} 원".format(i+1, payment))

if __name__ == "__main__":
    main()
