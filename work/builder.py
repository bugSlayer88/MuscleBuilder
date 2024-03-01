import csv
import random

# equipment = ['Full Gym', 'At Home w Weights', 'At Home No Weights']

# open csv from sql and read lines
with open('exercise_info.csv', mode='r') as file:
    exercise_file = csv.reader(file)
    exercise_lines = []
    for lines in exercise_file:
        exercise_lines.append(lines)
# list chest exercises
chest_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Chest':
        chest_focus.append(exercise_lines[i][1])
# list tricep exercises
tri_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Triceps':
        tri_focus.append(exercise_lines[i][1])
# list bicep exercises
bi_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Biceps':
        bi_focus.append(exercise_lines[i][1])
# list shoulder exercises
shoulder_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Shoulders':
        shoulder_focus.append(exercise_lines[i][1])
# list back exercises
back_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Back':
        back_focus.append(exercise_lines[i][1])
# list glute exercises
glute_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Glutes':
        glute_focus.append(exercise_lines[i][1])
# list leg exercises
leg_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Legs':
        leg_focus.append(exercise_lines[i][1])
# list ab exercises
ab_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][5] == 'Abs':
        ab_focus.append(exercise_lines[i][1])
# list cardio/heart exercises
heart_focus = []
for i in range(len(exercise_lines)):
    if exercise_lines[i][2] == 'Heart':
        heart_focus.append(exercise_lines[i][1])

with open('routine_details.csv', mode='r') as file:
    routine_file = csv.reader(file)
    routine_lines = []
    for lines in routine_file:
        routine_lines.append(lines)
# list exercises for weights at home
weights_at_home = []
for i in range(len(routine_lines)):
    if (routine_lines[i][4] != 'Pull Up Bar' and routine_lines[i][4] != 'Incline Bench' and
            routine_lines[i][4] != 'Cable' and routine_lines[i][4] != 'Machine' and routine_lines[i][4] != 'equipment'):
        weights_at_home.append(routine_lines[i][0])
# list exercises for no weights at home
at_home_no_weights = []
for i in range(len(routine_lines)):
    if (routine_lines[i][4] == 'Resistance Band' or routine_lines[i][4] == 'Medicine Ball' or
            routine_lines[i][4] == 'None'):
        at_home_no_weights.append(routine_lines[i][0])
# exercises for full gym
gym = []
for i in range(len(routine_lines)):
    if routine_lines[i][4] != 'equipment':
        gym.append(routine_lines[i][0])


class GetWorkouts():

    def __init__(self, split_pref, focus_pref):
        self.split_pref = split_pref
        self.focus_pref = focus_pref

        self.all_upper = chest_focus + tri_focus + bi_focus + shoulder_focus + back_focus
        self.all_lower = glute_focus + leg_focus
        self.all_full_body = chest_focus + tri_focus + bi_focus + shoulder_focus + back_focus + glute_focus + leg_focus

        self.chest_focus = chest_focus
        self.tri_focus = tri_focus
        self.bi_focus = bi_focus
        self.shoulder_focus = shoulder_focus
        self.back_focus = back_focus
        self.glute_focus = glute_focus
        self.leg_focus = leg_focus


    def warm_up_moves(self):
        warm_ups = []
        for i in range(0, 1):
            rand_cardio = random.choice(heart_focus)
            warm_ups.append(rand_cardio)
        return warm_ups

    def ab_moves(self):
        # ab_moves_end = []
        # for i in range(0,2):
        rand_ab = random.sample(ab_focus, 2)
        # ab_moves_end.append(rand_ab)
        return rand_ab

    def main_focus_moves(self):
        if self.focus_pref == 'Chest':
            return self.chest_focus
        elif self.focus_pref == 'Triceps':
            return self.tri_focus
        elif self.focus_pref == 'Biceps':
            return self.bi_focus
        elif self.focus_pref == 'Shoulders':
            return self.shoulder_focus
        elif self.focus_pref == 'Back':
            return self.back_focus
        elif self.focus_pref == 'Glutes':
            return self.glute_focus
        elif self.focus_pref == 'Legs':
            return self.leg_focus

    def secondary_focus_moves(self):
        main_focus_upper = ['Chest', 'Shoulders', 'Triceps', 'Biceps', 'Back']
        main_focus_lower = ['Legs', 'Glutes']
        if self.split_pref == 'Upper Body':
            second_focus_upper = list(filter(lambda x: x != self.focus_pref, main_focus_upper))
            secondary_focus_rand = random.choice(second_focus_upper)
            if secondary_focus_rand == 'Chest':
                return self.chest_focus
            elif secondary_focus_rand == 'Triceps':
                return self.tri_focus
            elif secondary_focus_rand == 'Biceps':
                return self.bi_focus
            elif secondary_focus_rand == 'Shoulders':
                return self.shoulder_focus
            elif secondary_focus_rand == 'Back':
                return self.back_focus
        elif self.split_pref == 'Lower Body':
            # main_focus_lower = ['Legs', 'Glutes']
            second_focus_lower = list(filter(lambda x: x != self.focus_pref, main_focus_lower))
            secondary_focus_rand = random.choice(second_focus_lower)
            if secondary_focus_rand == 'Legs':
                return self.leg_focus
            elif secondary_focus_rand == 'Glutes':
                return self.glute_focus
        elif self.split_pref == 'Full Body':
            if self.focus_pref in main_focus_upper:
                second_focus_full = random.choice(main_focus_lower)
                if second_focus_full == 'Legs':
                    return self.leg_focus
                elif second_focus_full == 'Glutes':
                    return self.glute_focus
            if self.focus_pref in main_focus_lower:
                second_focus_full = random.choice(main_focus_upper)
                if second_focus_full == 'Chest':
                    return self.chest_focus
                elif second_focus_full == 'Triceps':
                    return self.tri_focus
                elif second_focus_full == 'Biceps':
                    return self.bi_focus
                elif second_focus_full == 'Shoulders':
                    return self.shoulder_focus
                elif second_focus_full == 'Back':
                    return self.back_focus


# home_weights_set = set(weights_at_home)
# print(home_weights_set)
# chest_as_set = set(chest_focus)
# print(chest_as_set)
# chest_home = home_weights_set - chest_as_set
# print(chest_home)
# print(home_weights_set.intersection(chest_as_set))
