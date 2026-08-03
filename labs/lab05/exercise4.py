item_name = input("item name: ")
item_price = float(input("item price: "))

quantity = 3
tax_rate = 0.06

subtotal = item_price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

print( subtotal , tax_amount , total_cost )
