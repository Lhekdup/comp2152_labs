'''
Author: <Lhekdup Tenzin>
Assignment: #1
'''

gym_member = "Alex Alliton"         #string
preferred_weight_kg = 20.5          #float
highest_reps = 25                   #int
membership_active = True            #boolean

#dict
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (29, 39, 10),
    "Taylor": (40, 35, 30)
}
print(workout_stats)
'''
total_workout_minutes = {}
for name, minute in workout_stats.items():
    total_workout_minutes.update({name+"_Total": sum(minute)})
    
print(total_workout_minutes)
'''

for name, minute in workout_stats.items():
    workout_stats[name+"_Total"] = workout_stats.pop(name)
    workout_stats.update({name + "_Total": sum(minute)})

print(workout_stats)

names = list(workout_stats.keys())
minutes = list(workout_stats.values())
workout_list = []
for i in range(0, len(names)):
    workout_list.append(names[i])
    for j in range(0, len(minutes)):
        workout_list.append("yoga")
        workout_list.append("running")
        workout_list.append("weightlifting")



print(workout_list)

'''
names = list(workout_stats.keys())
minutes = list(workout_stats.values())
workout_list = []
for i in range(0, len(names)):
    workout_list.append(names[i])
    workout_list.append(minutes[i])

print(workout_list)



first_two = [row[1] for row in workout_list]
#first_tw = list(workout_list.items()[:2])
for i in range(0, 4, 2):
    x = slice(1,4,2)
    print(workout_list[x])
'''

#y = slice(2)
#print(first_two)

