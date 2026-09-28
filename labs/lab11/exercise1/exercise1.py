speed = int(input())
total_readings = 0
longest_streak = 0
current_streak = 0

while speed != -1:
    total_readings = total_readings + 1 
    if speed < 20:
        longest_streak = longest_streak + 1
    else:
        longest_streak = 0

    if longest_streak >=current_streak:
        current_streak = longest_streak

    speed = int(input())
    
longest_streak = current_streak
print(total_readings)
print(longest_streak)
