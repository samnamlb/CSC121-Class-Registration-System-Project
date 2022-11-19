# ----------------------------------------------------------------
# Author:Angelica West
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------
#import student
#import billing
from student2 import *
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

    # what i've done wrong so far:
    #1. while answer != '0 'or id != '0': means when this is true then do everything inside of me
    # if it isn't true then stop so: if answer != '0' & break isn't needed
    #2.if you want len to go first you have to write if len(id) != 4 otherwise it's good where it's at
    # should indent lines 62-71 to be underneath answer = input('')
    # else if id not in idNum print incorrect pass or pin and start again
    id = " "
    answer = ''
    while answer != '0' or id != '0':
        id = input("Enter ID to log in, or 0 to quit: ")
        for idNum, pin in student_list:
            if id in idNum:
                if len(id) == 4:
                    login(id, student_list)
                else:
                    print("Incorrect Id or Pin.")
                    break

                answer = input("Enter 1 to add course, 2 to drop course, 3 to list courses, 4 to show bill, 0 to exit: ")
                if answer == '1':
                    # add_course()
                    add_course(id, course_roster, course_max_size)
                elif answer == '2':
                    drop_course(id, course_roster)
                    # drop_course()
                elif answer == '3':
                   list_courses(id, course_roster)
                elif answer == '4':
                    display_bill(id, student_in_state, course_roster, course_hours)


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. *****If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    # pass  # temporarily avoid empty function definition
    # My code so far:
    pin = input("Enter PIN: ")
    for ids, pinNum in s_list:
        if pin in pinNum:
            if len(pin) == 3:
                print("Login and pin verified!")
                break
        else:
            print("ID or pin incorrect.")
            pin = input("Enter PIN: ")

main()
