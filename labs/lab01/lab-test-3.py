monthly_usage = float(input("enter monthly usage:"))

if monthly_usage < 50:
    bill = monthly_usage
elif monthly_usage <= 100:
    bill = monthly_usage - (monthly_usage * 0.05)
else:
    bill = 50 + 50 * 0.05 + (monthly_usage -100) * 0.2

print(f"amount of the bill to be paid: {bill:.2f}")