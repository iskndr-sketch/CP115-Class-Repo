income = float(input())
if income <= 50000:
    tax = 0
else:
    if income <= 100000:
        tax = 0.01
    else:
        tax = 0.02
totaltax = income * tax
print(toatalTax)
