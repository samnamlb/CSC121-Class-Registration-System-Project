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
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has two parameters: id is the ID of the
    # student; c_roster is the list of class rosters. This function
    # has no return value.
    # -------------------------------------------------------------

    # Accumulator for courses registered
    num_courses = 0

    # Add number of courses
    print('Courses registered:')
    for keys, value in c_roster.items():
        if id in value:
            print(keys)
            num_courses += 1
    print(f'Total number: {num_courses}\n')


def add_course(id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    # Have user enter a course code
    course = input("Enter course you want to add: ")
    if course not in c_roster:
        print('Course not found.\n')
    elif id in c_roster[course]:
        print('You are already enrolled in that course.\n')
    elif len(c_roster[course]) >= c_max_size[course]:
        print('Course already full.\n')
    else:
        # Add student to course
        course_list = c_roster[course]
        course_list.append(id)
        c_roster[course] = course_list
        print('Course added.\n')


def drop_course(id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------

    # Drops courses
    course = input("Enter course you want to drop: ")
    if course not in c_roster:
        print('Course not found.\n')
    elif id not in c_roster[course]:
        print('You are not enrolled in that course.\n')
    else:
        # Remove student from the specified course
        c_roster[course].remove(id)
        print('Course dropped.\n')
