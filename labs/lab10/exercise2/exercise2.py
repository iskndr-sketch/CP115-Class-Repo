num_days = int(input())
danger_threshold = float(input())

total_temp = 0
danger_days = 0

for i in range(num_days):
    daily_temperture = float(input("Enter temperature: "))
    total_temp = total_temp + daily_temperture
    if daily_temperture > danger_threshold:
        danger_days = danger_days + 1
  

average_temp = total_temp / num_days



print(danger_days)
print(f"{average_temp:.1f}")
