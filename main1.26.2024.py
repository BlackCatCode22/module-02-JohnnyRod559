def compute_pay(hours, rate) :
    print("In computepay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning", pay)
    return pay

hours_worked = input("Enter Hours: ")
pay_rate = input("Rate: ")
float_hours = float(hours_worked)
float_rate = float(pay_rate)
#print(float_hours, float_rate)

total_pay = compute_pay(float_hours, float_rate)

print("Pay: ", total_pay)
