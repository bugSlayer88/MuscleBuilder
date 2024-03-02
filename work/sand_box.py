import csv

with open('exercise_info.csv', mode='r') as file:
    exercise_file = csv.reader(file)
    exercise_lines = []
    for lines in exercise_file:
        exercise_lines.append(lines)

with open('routine_details.csv', mode='r') as file:
    routine_file = csv.reader(file)
    routine_lines = []
    for lines in routine_file:
        routine_lines.append(lines)

print(routine_lines)
print(routine_lines[4][4])

class WorkOutInfo:
    def __init__(self, work_out_move):
        self.work_out_move = work_out_move

    def primary_muscle(self):
        get_pri_muscle = []
        for i in range(len(exercise_lines)):
            if exercise_lines[i][1] == self.work_out_move:
                get_pri_muscle.append(exercise_lines[i][2])
        return get_pri_muscle[0]

    def equipment(self):
        get_equip = []
        for i in range(len(routine_lines)):
            if routine_lines[i][0] == self.work_out_move:
                get_equip.append(routine_lines[i][4])
        return get_equip[0]


fave = WorkOutInfo('Forward Lunges')

print(fave.primary_muscle())
print(fave.equipment())

