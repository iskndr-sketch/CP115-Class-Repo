hours = float(input())
if hours <= 2:
    parkingFee = 0
else:
    if hours < 5:
        parkingFee = (hours - 2) * 2
    else:
        parkingFee = (hours - 5) * 3 + 6
if parkingFee >= 30:
    parkingFee = 30
else:
    parkingFee = parkingFee
print(parkingFee)
