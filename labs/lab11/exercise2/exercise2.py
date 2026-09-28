score = int(input())
total_a = 0
total_b = 0
count = 0

while score != -1:
    count = count + 1
    if count % 2 == 1:
       total_a = total_a + score
    else:
        total_b = total_b + score
    score = int(input())


if total_a > total_b:
     winner = "A"
elif total_b > total_a:
     winner = "B"
else:
    winner = "Tie"

print(total_a)
print(total_b)
print(winner)
