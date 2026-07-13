kwh = float(input())
if kwh <= 100:
    totalBill = kwh * 0.3
else:
    if kwh < 200:
        totalBill = (kwh - 100) * 0.5 + (100 * 0.30)
    else:
        totalBill = (kwh - 200 )* 0.75 + (100 * 0.5) + (100 * 0.30)
print(totalBill)
