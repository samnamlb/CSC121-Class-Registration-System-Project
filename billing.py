# ----------------------------------------------------------------
# Author:
# Date:
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
from datetime import datetime
# datetime is a module that gives you class's of time/date
# datetime class allows you to use the .now() method to  return the date and time with time zone(optional/ if want to use add as an argument)
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
    # pass  # temporarily avoid empty function definition
    total_hours = 0
    total_cost = 0.0
    generated_on = datetime.now()
    generated_on = generated_on.strftime("%Y-%m-%d %H:%M:%S")
    print("Tuition Summary")
    # print(f' Student {id}, {s_in_state[id]}')
    if s_in_state[id] == True:
        print(f"Student {id}: In state")
        for key , value in c_rosters.items():
            # if id in value:
            if id in value:
                # print(f'key: {key}')
                for k,v in c_hours.items():
                    if key in k:
                        # print(f'value:  {v}')
                        total_hours = total_hours + v
                        cost = 225 * v
                        total_cost = total_cost + cost
                        print(f'Generated on {generated_on}')
                        print(f"Course       Hours      Cost")
                        print("--------    --------  -------")
                        print(f'{key}            {v}   ${cost:.2f} ')
                        print('------ --------- ----------')

                # this works too!
                # if key in c_hours.keys():
                #     print(f'{c_hours[key]}')
                    # print(f"This is k: {k}")
# It's possible to just do one for loop instead of many(for loops)(it's actually better space) ---just add
    # an if statement instead of the for loop and instead a specific value or key add a :
    # if first_for_loop_key/value_variable in complex_data_or_just_like_a_dicionary

# To understand how to unpack this code try loops and if statements try .items() or .keys() or .values()
# for each statement / line of could you try print it to see if it's the value you want

    # course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    # course_roster = {'CSC101': ['1004', '1003'],
    #                  'CSC102': ['1001'],
    #                  'CSC103': ['1002'],
    #                  'CSC104': []}


            # for course, hours in c_hours.items():
            #
            #         total_hours = total_hours + hours
            #         cost = 225 * hours
            #         total_cost = total_cost + cost
            #         print(f'Generated on {generated_on}')
            #         print(f"Course       Hours      Cost")
            #         print("--------     --------   -------")
            #         print(f'{key}  {hours}  ${cost:.2f} ')
            #         print('------ --------- ----------')
    else:
        print(f"Student {id}: out of state")
        for key , value in c_rosters.items():
            # if id in value:
            if id in value:
                # print(f'key: {key}')
                for k,v in c_hours.items():
                    if key in k:
                        # print(f'value:  {v}')
                        total_hours = total_hours + v
                        cost = 850 * v
                        total_cost = total_cost + cost
                        print(f'Generated on {generated_on}')
                        print(f"Course       Hours      Cost")
                        print("--------    --------  -------")
                        print(f'{key}            {v}   ${cost:.2f} ')
                        print('--------    --------   -------')
    print(f'Total         {total_hours}     ${total_cost:.2f}')
        # for key, value in c_rosters.items():
        #     for course, hours in c_hours.items():
        #         if id in c_rosters:
        #             total_hours = total_hours + hours
        #             cost = 850 * hours
        #             total_cost = total_cost + cost
        #             print(f'Generated on {generated_on}')
        #             print(f"Course       Hours      Cost")
        #             print("--------     --------   -------")
        #             print(f'{key}  {hours}  ${cost:.2f} ')
        #             print('------   --------- ----------')
    # print(f'Total         {total_hours}     ${total_cost:.2f}')


#--------would this work:
        # for key, value in c_rosters.items():
        #     for course, hours in c_hours.items():
        #         if id in c_rosters:
        #             if key in course:
                    #     print(f' This is hours: {hours}')
        #               total_hours = total_hours + hours
        #               cost = 850 * hours
        #               total_cost = total_cost + cost
        #               print(f'Generated on {generated_on}')
        #               print(f"Course       Hours      Cost")
        #               print("--------     --------   -------")
        #               print(f'{key}  {hours}  ${cost:.2f} ')
        #               print('------   --------- ----------')
    # print(f'Total         {total_hours}     ${total_cost:.2f}')


    # print(f'Generated on')
    # print(f"Course       Hours      Cost")
    # print("--------     --------   -------")
    # for key, value in c_rosters.items():
    #     if id in c_rosters:
    #     # maybe instead write if id in value
    #     # this should print the value for
    #         print(f" {c_rosters[key]}")
# i got this error: NameError: name 's_in_state' is not defined b/c if statement was NOT INDENTED
#     if s_in_state[id] == True:
#         print(f" Student {id},Tuition Summary In state")
#     else:
#         print(f" Student {id},Tuition Summary out of state")
#     print(f'Generated on')
#     print(f"Course       Hours      Cost")
#     print("--------     --------   -------")
#     for key,value in c_rosters.items():
#     # # now we have to figure out how to display values with only a specific id this doesn't work... if c_roster[key] == id:
#     #     #print(key)
#         if value == id:
#             key = var
#             print(f"key from c_roster: {key}")
#         for ke, val in c_hours.items():
#             if var in c_hours:
#                 val = hour
#                 print(val)


    # student_list = [('1001', '111'), ('1002', '222'),
    #                 ('1003', '333'), ('1004', '444')]
    # student_in_state = {'1001': True,
    #                     '1002': False,
    #                     '1003': True,
    #                     '1004': False}
    #
    # course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    # course_roster = {'CSC101': ['1004', '1003'],
    #                  'CSC102': ['1001'],
    #                  'CSC103': ['1002'],
    #                  'CSC104': []}
    # course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
# SC101        3  $ 675.00
# CSC102        4  $ 900.00
# CSC104        3  $ 675.00

