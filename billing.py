# ----------------------------------------------------------------
# Author: Angelica West & Aleem Azimov
# Date:
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
from datetime import datetime


# datetime is a module that gives you class's of time/date
# datetime class allows you to use the .now() method to  return the date and time with time zone(optional)/ if want to use add as an argument)
# .strftime(format) function  formats the date / time to whatever you like
# ex--(if using a now method) variable.strftime("%Y-%m-%d %H:%M:%S")
# use a string and ('%Y,%m,%d,%H,%M,%S represents the (year,month,day,hour,minute,second)
# (by using format code for the strfrtime() function/ that's why there is a %)
# example %Y =' 2015' (so has 4 digits) and %y = '97' (so only shows/ formats year with two decimal places)
# --Whatever you put between them is how each type of specific time/date is formatted
# strfrtime function = string format time & it used to convert date and time objects to their string form


def display_bill(id, s_in_state, c_rosters, c_hours):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------
    total_hours = 0
    total_cost = 0.0
    generated_on = datetime.now()
    generated_on = generated_on.strftime("%Y-%m-%d %H:%M:%S")
    print("Tuition Summary")
    # print(f' Student {id}, {s_in_state[id]}')
    print(f'Generated on {generated_on}')
    if s_in_state[id]:
        print(f"Student {id}: In-State Student")
        print("Course    Hours    Cost")
        print("------    -----  --------")
        for key, value in c_rosters.items():
            # if id in value:
            if id in value:
                # print(f'key: {key}')
                for k, v in c_hours.items():
                    if key in k:
                        # print(f'value:  {v}')
                        total_hours = total_hours + v
                        cost = 225 * v
                        total_cost = total_cost + cost
                        print(f'{key}{v:>9}  ${cost:>7.2f} ')
    else:
        print(f"Student {id}: Out-of-State Student")
        print("Course    Hours    Cost")
        print("------    -----  --------")
        for key, value in c_rosters.items():
            # if id in value:
            if id in value:
                # print(f'key: {key}')
                for k, v in c_hours.items():
                    if key in k:
                        # print(f'value:  {v}')
                        total_hours = total_hours + v
                        cost = 850 * v
                        total_cost = total_cost + cost
                        print(f'{key}{v:>9}  ${cost:>7.2f} ')
    print('        -------  --------')
    print(f'Total{total_hours:>10}  ${total_cost:>7.2f}\n')
