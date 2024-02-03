hours_worked = input("Enter Hours: ")
pay_rate = input("Rate: ")
try:
    float_hours = float(hours_worked)
    float_rate = float(pay_rate)
except:
    print("Error, please enter numeric input")
    quit()

print(float_hours, float_rate)
if float_hours > 40:
    reg = float_rate * float_hours
    otp = (float_hours - 40.0) * (float_rate * 0.5)
    total_pay = reg + otp
else:
    total_pay = float(hours_worked) * float(pay_rate)
print("Pay: ", total_pay)
