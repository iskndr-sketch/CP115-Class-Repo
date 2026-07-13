income = float(input())
if income <= 50000:
    totalTax = 0
else:
    if income >= 100000:
        totalTax = (income - 100000) * 0.02 + (50000 * 0.01)
    else:
        totalTax = (income - 50000) * 0.01
print(totalTax)
