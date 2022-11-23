# ----------------------------------------------------------------
# Author: Angelica West & Aleem Azimov
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
from student import *
from billing import *


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]
    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}

    while True:
        student_id = input("Enter ID to log in, or 0 to quit: ")
        if student_id == '0':
            break
        else:
            is_logged = login(student_id, student_list)
            if is_logged:
                while True:
                    answer = input(
                        "Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                    if answer == '0':
                        print('Session ended.\n')
                        break
                    else:
                        if answer == '1':
                            # add_course()
                            add_course(student_id, course_roster, course_max_size)
                        elif answer == '2':
                            drop_course(student_id, course_roster)
                            # drop_course()
                        elif answer == '3':
                            # list_course()
                            list_courses(student_id, course_roster)
                        elif answer == '4':
                            # display_bill
                            display_bill(student_id, student_in_state, course_roster, course_hours)
            else:
                continue


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    found = False
    pin = input("Enter PIN: ")
    for student in s_list:
        if student[0] == id and student[1] == pin:
            found = True
            break
        else:
            found = False
    # Output verify if login successful, else show error
    if found:
        print("Login and pin verified!\n")
    else:
        print("ID or pin incorrect.\n")
    return found


main()
