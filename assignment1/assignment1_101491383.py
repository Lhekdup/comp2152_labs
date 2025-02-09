#a
"""
Author: <Lhekdup Tenzin>
Assignment: #1
"""

#b
gym_member = "Alex Alliton"         #string
preferred_weight_kg = 20.5          #float
highest_reps = 25                   #int
membership_active = True            #boolean

#c
workout_stats = {
    "Alex": (30, 45, 50),
    "Jamie": (29, 39, 10),
    "Taylor": (60, 44, 30)
}
print(workout_stats)                #dict

#d
total_workout_stat = {}
for name, minute in workout_stats.items():
    total_workout_stat.update({name + "_Total": sum(minute)})

print(total_workout_stat)           #dict

#e
names = list(workout_stats.keys())
workout_list = []
for i in range(0, len(names)):
    exercises = [names[i]]
    for j in range(0, len(names)):
        if j == 0:
            exercises.append("yoga")
        elif j == 1:
            exercises.append("running")
        else:
            exercises.append("weightlifting")
    workout_list.append(exercises)
print(workout_list)                   #list

#f
yoga_running = []
for name, minute in workout_stats.items():
    yoga_running.append({name : minute[:2]})
print(yoga_running)

last_two = []
for name, minute in workout_stats.items():
    last_two.append({name: minute})
last_two.pop(0)
print(last_two)

#g
for name, minute in workout_stats.items():
    if sum(minute) >= 120:
        print("Great Job staying active " + name + "!")

#h
username = input("Enter a friend's name: ")
if username in workout_stats:
    print(workout_stats[username])
    for name, minute in workout_stats.items():
        workout_stats.update({name: sum(minute)})
    print(workout_stats[username])
else:
    print("Friend " + username + " not found in the record!.")

#i
highest_total_minutes = max(total_workout_stat, key=total_workout_stat.get)
lowest_total_minutes = min(total_workout_stat, key=total_workout_stat.get)
h = highest_total_minutes[:-6]
l = lowest_total_minutes[:-6]
print(h, "has the highest total workout minutes and" ,l, "has the lowest total workout minutes.")














