num_rounds = int(input(" "))

final_score = 0
rounds_processed = 0

for _ in range(num_rounds):
    round_score = float(input("Enter round score: "))
    final_score += round_score
    if final_score > 100:
        final_score = final_score + (final_score * 0.2)
    rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)
