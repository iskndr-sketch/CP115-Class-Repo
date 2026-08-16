coffe=3.50
muffin=2.10
water=1.05


totalcoffe=2*coffe
totalmuffin=3*muffin
totalwater=4*water

subtotal=totalmuffin+totalmuffin+totalwater
tax=0.06*subtotal
total=subtotal+tax

print(f"========== RECEIPT ==========\nItem\tPrice\tQty\ttotal\nCoffee\t${coffe}\t2\t${totalcoffe}\nMuffin\t${muffin}\t3\t{totalmuffin}\nWater\t${water}\t4\t${totalwater}\n-----------------\nSubtotal\t\t${subtotal}\ntax(6%)\t\t{tax}\nTotal\t\t{total}\n============================")
