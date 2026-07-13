weight = float(input())
ticketPrice = float(input())
if weight > 0:
    if weight > 15:
        finalPrice = ticketPrice + weight - 15 * 4
    else:
        finalPrice = ticketPrice + 0
else:
    finalPrice = ticketPrice - 10
print(finalPrice)
