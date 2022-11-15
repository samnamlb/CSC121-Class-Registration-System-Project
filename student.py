# ----------------------------------------------------------------
# Author: Aleem Azimov
# Date: 11/12/2022
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(id, c_roster):
    num_courses = 0
    course_names = []
    for keys, value in c_roster.items():
        if id in value:
            course_names.append(keys)
            num_courses += 1

    if num_courses > 1:
        print(f'Registered to {num_courses} courses')
    elif num_courses < 1:
        print(f'Registered to no courses')
    else:
        print(f'Registered to {num_courses} course')
    print('----------------------')
    for course in course_names:
        print(f'{course}')


def add_course(id, c_roster, c_max_size):
    while True:
        course = input("Enter the course you would like: ")
        if course not in c_roster:
            print('Course not offered.')
        elif id in c_roster[course]:
            print('Student already registered for this course.')
        elif len(c_roster[course]) >= c_max_size[course]:
            print('Course is full.')
        else:
            break
    course_list = c_roster[course]
    course_list.append(id)
    c_roster[course] = course_list


def drop_course(id, c_roster):
    while True:
        course = input("Enter the course you would like to drop: ")
        if course not in c_roster:
            print('Course not offered.')
        elif id not in c_roster[course]:
            print('Student not in course.')
        else:
            break
    c_roster[course].remove(id)
