target_points = int(input())

total_points = 0
rounds_played = 0

while total_points < target_points:
    round_score = float(input("enter round score: "))
    total_points = total_points + round_score
    rounds_played = rounds_played + 1


print(total_points)
print(rounds_played)
