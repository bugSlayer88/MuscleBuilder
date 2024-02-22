#
# # CREATE TABLE exercise_info (
# # 	workout_id SERIAL PRIMARY KEY,
# # 	workout_title varchar(50) UNIQUE,
# # 	primary_muscle varchar(100),
# # 	secondary_muscle varchar(100),
# # 	alt_name_01 varchar(100)
# # );
#
# # want to add these in other table:
# # 	focus_category varchar(20),
# # 	workout_type varchar(15),
# # 	routine_spot varchar(10))
#

# update other tables when new workouts are added to main list
# INSERT INTO routine_details(workout_title)
# SELECT workout_title
# FROM exercise_info
# WHERE exercise_info.workout_title NOT IN (SELECT workout_title FROM routine_details);