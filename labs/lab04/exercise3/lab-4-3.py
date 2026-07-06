hours = float(input())
if hours <= 2:
    fee = 0
else:
    if hours <= 5:
        fee = 2
    else:
        fee = 3
parkingFee = hours * fee
if parkingFee >= 30:
    parkingFee = 30
print(parkingFee)
