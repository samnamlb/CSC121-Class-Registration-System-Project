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
    # Accumulator for courses registered
    num_courses = 0
    # List of course code names
    course_names = []
    # Add number of courses found where the student is registered in the roster
    for keys, value in c_roster.items():
        if id in value:
            course_names.append(keys)
            num_courses += 1

    # Grammar check, plural 'courses' vs. singular 'course' based on num_courses
    if num_courses > 1:
        print(f'Registered to {num_courses} courses')
    elif num_courses < 1:
        print(f'Registered to no courses')
    else:
        print(f'Registered to {num_courses} course')
    print('----------------------')
    # Display all registered courses
    for course in course_names:
        print(f'{course}')


def add_course(id, c_roster, c_max_size):
    # Have user enter a course code
    while True:
        course = input("Enter the course you would like: ")
        # When course is not found in the roster
        if course not in c_roster:
            print('Course not offered.')
        # When the student is already found at the specified course
        elif id in c_roster[course]:
            print('Student already registered for this course.')
        # When the course is full due to the max size from c_max_size dictionary
        elif len(c_roster[course]) >= c_max_size[course]:
            print('Course is full.')
        else:
            # Exit out of loop if no errors occurred
            break
    # Makes the value of the courses in the roster into an editable list
    course_list = c_roster[course]
    # Adds student to course
    course_list.append(id)
    # Puts the course list back as a value to the roster
    c_roster[course] = course_list


def drop_course(id, c_roster):
    while True:
        course = input("Enter the course you would like to drop: ")
        # If course is not found in roster
        if course not in c_roster:
            print('Course not offered.')
        # If the student based by id is not found in the roster
        elif id not in c_roster[course]:
            print('Student not in course.')
        else:
            # Exit out of loop if no errors occurred
            break
    # Remove student from the specified course
    c_roster[course].remove(id)
