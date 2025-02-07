'''
Author: <Lhekdup Tenzin>
Assignment: #1
'''

gym_member = "Alex Alliton"         #string
preferred_weight_kg = 20.5          #float
highest_reps = 25                   #int
membership_active = True            #boolean

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (29, 39, 10),
    "Taylor": (40, 35, 30)
}
print(workout_stats)                #dict

for name, minute in workout_stats.items():
    workout_stats[name+"_Total"] = workout_stats.pop(name)
    workout_stats.update({name + "_Total": sum(minute)})

print(workout_stats)                #dict

names = list(workout_stats.keys())
minutes = list(workout_stats.values())
workout_list = []
for i in range(0, len(names)):
    exercises = []
    exercises.append(names[i])
    for j in range(0, len(minutes)):
        if (j == 0):
            exercises.append("yoga")
        elif (j == 1):
            exercises.append("running")
        else:
            exercises.append("weightlifting")
    workout_list.append(exercises)
print(workout_list)                     # list


#y = slice(2)
#print(first_two)

