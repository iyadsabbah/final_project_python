import defs

students_list = []
course_list = []

while True:
    selected = input('''
    Enter The number of your choice 
    1.Add New Student 
    2.Remove Student 
    3.Edit Student 
    4.Display All Students 
    5.Create New Course 
    6.Add course to student
    7.exit  
    ''')
    if selected == '1':
        defs.add_new_student(students_list)

    elif selected == '2':
        defs.remove_student(students_list)

    elif selected == '3':
        defs.edit_student(students_list)

    elif selected == '4':
        defs.display_all_students(students_list)

    elif selected == '5':
        defs.add_new_course(course_list)

    elif selected == '6':
        defs.add_course_to_student(students_list, course_list)

    elif selected == '7':
        print('''
        -------------------------------------
        ------------- Goodbye ---------------
        -------------------------------------
        ''')
        exit()
    else:
        print('Please enter a valid number from the list')
